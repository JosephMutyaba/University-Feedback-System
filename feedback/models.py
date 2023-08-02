from django.db import models

class College(models.Model):
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name

class School(models.Model):
    school_name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    student_number = models.CharField(max_length=50, unique=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    current_year_of_study = models.PositiveIntegerField()
    current_semester = models.CharField(max_length=10)
    course_unit_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    facility_name = models.CharField(max_length=100)
    facility_rating = models.PositiveIntegerField()
    facility_comments = models.TextField()
    lecturer_name = models.CharField(max_length=100)
    lecturer_rating = models.PositiveIntegerField()
    lecturer_comments = models.TextField()
    suggestions = models.TextField()

    def __str__(self):
        return f"Feedback by {self.student.student_name} - {self.course_unit_name}"

