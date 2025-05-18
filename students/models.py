from django.db import models
from courses.models import Course

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    registration_number = models.CharField(max_length=20, unique=True)
    enrolled_courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Guardian(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

