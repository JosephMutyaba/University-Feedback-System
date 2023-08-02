from django.contrib.auth.backends import ModelBackend
from .models import Student

class StudentNumberBackend(ModelBackend):
    def authenticate(self, student_name=None, student_number=None):
        try:
            student = Student.objects.get(student_name=student_name, student_number=student_number)
            return student
        except Student.DoesNotExist:
            return None
