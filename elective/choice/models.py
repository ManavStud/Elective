from django.db import models

# Create your models here.
class Choice(models.Model):
    roll_no=models.CharField(max_length=8)
    pref_no=models.IntegerField()
    course=models.CharField(max_length=400)