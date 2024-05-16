from django.db import models

# Create your models here.


class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    mobile_number=models.IntegerField()
    create_at=models.DateTimeField(auto_now=True)
    employee_rig_number=models.TextField()

    