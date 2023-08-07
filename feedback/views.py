from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import StudentRegistrationForm, StudentLoginForm, FeedbackForm
from .models import Student, Feedback
from django.shortcuts import render, redirect, get_object_or_404


def launch_view(request):
    return render(request, 'feedback/launch.html')


def login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            student_number = form.cleaned_data['student_number']

            try:
                # Manually authenticate the student based on student_name and student_number
                student = Student.objects.get(student_name=student_name, student_number=student_number)
            except Student.DoesNotExist:
                student = None

            if student is not None:
                # If the student exists, create a custom session for the user
                request.session['student_id'] = student.id
                return redirect('display_content')
            else:
                form.add_error(None, 'Invalid student name or student number.')
    else:
        form = StudentLoginForm()
    return render(request, 'feedback/login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('login')

def feedback_form_view(request):
    # Check if the user is logged in by verifying the custom session key
    if 'student_id' in request.session:
        student_id = request.session['student_id']
        try:
            # Retrieve the student object based on the custom session key
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            student = None

        if student is not None:
            # If the user is logged in, proceed with the feedback form logic here
            if request.method == 'POST':
                form = FeedbackForm(request.POST)
                if form.is_valid():
                    # Save the feedback form data associated with the logged-in student
                    feedback = form.save(commit=False)
                    feedback.student = student
                
                    feedback.save()

                    return redirect('display_content')

            else:
                form = FeedbackForm()

            return render(request, 'feedback/feedback_form.html', {'form': form})

    # If the user is not logged in or the custom session key is invalid, redirect to the login page
    return redirect('login')


#@login_required
# def display_content_view(request):
#     feedbacks = Feedback.objects.filter(student=request.user)
#     return render(request, 'feedback/display_content.html', {'feedbacks': feedbacks})

def display_content_view(request):
    # Check if the user is logged in by verifying the custom session key
    if 'student_id' in request.session:
        student_id = request.session['student_id']
        try:
            # Retrieve the student object based on the custom session key
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            student = None

        if student is not None:
            # If the user is logged in, we proceed with the display content logic here
            # retrieve feedback submissions associated with the logged-in student
            feedback_submissions = Feedback.objects.filter(student=student)
            return render(request, 'feedback/display_content.html', {'feedback_submissions': feedback_submissions})

    # If the user is not logged in or the custom session key is invalid, redirect to the login page
    return redirect('login')


def registration_view(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new student
            student = form.save()

            # Set the student_id session variable
            request.session['student_id'] = student.id

            return redirect('display_content')
    else:
        form = StudentRegistrationForm()
    return render(request, 'feedback/registration.html', {'form': form})


def edit_feedback_view(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, student_id=request.session.get('student_id'))
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('display_content')
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'feedback/edit_feedback.html', {'form': form})

def delete_feedback_view(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, student_id=request.session.get('student_id'))
    if request.method == 'POST':
        feedback.delete()
        return redirect('display_content')
    return render(request, 'feedback/delete_feedback.html', {'feedback': feedback})


