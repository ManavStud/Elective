from django.db import models
#from subject.models import subject

class student(models.Model):
    roll_no= models.CharField(max_length=20, primary_key=True)
    stud_name = models.CharField(max_length=60)
    dept = models.CharField(max_length=10)
    sem_pass = models.IntegerField()
    hon_min = models.CharField(max_length=20)
    kt = models.CharField(max_length=500)
    admit_year=models.IntegerField()
    opt_course=models.CharField(max_length=500)
    gpa=models.FloatField()


