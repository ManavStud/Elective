from django.db import models

# Create your models here.
class preference(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=15)
    sem=models.CharField(max_length=50)
    dept=models.CharField(max_length=30)
    # pref1=models.CharField(max_length=500)
    # pref2=models.CharField(max_length=500)
    # pref3=models.CharField(max_length=500)
    # pref4=models.CharField(max_length=500)
    # pref5=models.CharField(max_length=500)
    # pref6=models.CharField(max_length=500)
    # pref7=models.CharField(max_length=500)
    # pref8=models.CharField(max_length=500)