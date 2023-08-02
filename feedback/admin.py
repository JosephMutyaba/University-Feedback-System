from django.contrib import admin
from .models import College, School, Department, Course, Student, Feedback

admin.site.register(College)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Feedback)

