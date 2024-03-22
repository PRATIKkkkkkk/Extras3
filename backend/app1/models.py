from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):
    roll = models.IntegerField()
    course = models.CharField(max_length=40)
    fees = models.FloatField()
    created_time = models.DateTimeField(auto_add_now=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="names")