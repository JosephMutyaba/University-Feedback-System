import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import College, School, Department, Course, Student, Feedback

# Define a custom admin class for the Feedback model
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'current_year_of_study', 'current_semester',
                    'course_unit_name','course_code','facility_name', 
                    'facility_rating', 'facility_comments','lecturer_name',
                    'lecturer_rating','lecturer_comments','suggestions')
    actions = ['export_as_csv']  # Add custom actions to export selected feedbacks

    # Custom action to export selected feedbacks as CSV
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="feedbacks.csv"'
        writer = csv.writer(response)

        # Write header row
        writer.writerow(['student', 'current_year_of_study', 'current_semester', 'course_unit_name',
                         'course_code','facility_name', 'facility_rating', 'facility_comments',
                         'lecturer_name','lecturer_rating','lecturer_comments','suggestions'])

        # Write data rows
        for feedback in queryset:
            writer.writerow([feedback.student, feedback.current_year_of_study, feedback.current_semester,
                             feedback.course_unit_name, feedback.course_code,feedback.facility_name,
                             feedback.facility_rating, feedback.facility_comments,feedback.lecturer_name, 
                             feedback.lecturer_rating, feedback.lecturer_comments, feedback.suggestions])

        return response

    export_as_csv.short_description = "Export selected feedbacks as CSV"  # Display name for the custom action
    

# Register models with their custom admin classes
admin.site.register(College)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Feedback, FeedbackAdmin)  # Register Feedback model with custom admin class
