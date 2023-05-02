from django.db import models
from subject.models import subject

class student(models.Model):
    roll_no= models.CharField(max_length=20, primary_key=True)
    stud_name = models.CharField(max_length=60)
    dept = models.CharField(max_length=10)
    sem_pass = models.CharField(max_length=100)
    hon_min = models.CharField(max_length=20)
    kt = models.CharField(max_length=500)
    admit_year=models.CharField(max_length=4)
    opt_course=models.CharField(max_length=500)
    gpa=models.FloatField()
    email=models.CharField(max_length=50)
    class Meta:
        app_label = 'student'


class faculty(models.Model):
    fac_name=models.CharField(max_length=100)
    fac_email=models.EmailField(max_length=100)
    fc_dept=models.CharField(max_length=5)




