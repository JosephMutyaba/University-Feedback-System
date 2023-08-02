from django import forms
from .models import College, School, Department, Course, Feedback, Student
   
     
from django import forms
from .models import Student, College, School, Department, Course

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'registration_number', 'student_number', 'college', 'school', 'department', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Query the database to get the choices for each foreign key field
        colleges = College.objects.all()
        schools = School.objects.all()
        departments = Department.objects.all()
        courses = Course.objects.all()

        # Create ModelChoiceField for each foreign key field with the queryset as choices
        self.fields['college'].queryset = colleges
        self.fields['school'].queryset = schools
        self.fields['department'].queryset = departments
        self.fields['course'].queryset = courses
     
        
class StudentLoginForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    student_number = forms.CharField(max_length=20, widget=forms.PasswordInput)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['student', 'college', 'school', 'department', 'course']


