from django.db import models

class preference(models.Model):
    stud_name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    sem=models.IntegerField()
    dept=models.CharField(max_length=10)
    pref1=models.CharField(max_length=100)
    pref2=models.CharField(max_length=100)
    pref3=models.CharField(max_length=100)
    pref4=models.CharField(max_length=100)
    pref5=models.CharField(max_length=100)
    pref6=models.CharField(max_length=100)
    pref7=models.CharField(max_length=100)
    pref8=models.CharField(max_length=100)
    
    
class subject(models.Model):
    sub_id= models.CharField(max_length=20, primary_key=True)
    sub_name = models.CharField(max_length=100)
    dept=models.CharField(max_length=10)
    type = models.CharField(max_length=4)
    hm = models.CharField(max_length=40)
    sem=models.IntegerField()


class exposure_courses(models.Model):
    course_name = models.CharField(max_length=100)
    sem = models.IntegerField()


class honorminor(models.Model):
    degree_name = models.CharField(max_length=100)
    start_sem  = models.IntegerField()
    type = models.CharField(max_length=4)
    dept = models.CharField(max_length=15)

class student(models.Model):
    roll_no= models.CharField(max_length=20)
    stud_name = models.CharField(max_length=60)
    dept = models.CharField(max_length=100)
    sem_pass = models.CharField(max_length=100)
    hon_min = models.CharField(max_length=100)
    kt = models.CharField(max_length=500)
    admit_year=models.CharField(max_length=4)
    opt_course=models.CharField(max_length=500)
    gpa=models.FloatField()
    email=models.EmailField()
    
class faculty(models.Model):
    fac_name=models.CharField(max_length=100)
    fac_email=models.EmailField(max_length=100)
    fac_dept=models.CharField(max_length=5)