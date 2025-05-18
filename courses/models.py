from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)

    def __str__(self):
        return self.name
