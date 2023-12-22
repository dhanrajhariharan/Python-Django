from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
