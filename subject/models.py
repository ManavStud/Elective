from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator


class subject(models.Model):
    sub_id= models.CharField(max_length=100, primary_key=True)
    sub_name = models.CharField(max_length=100)
    dept=models.CharField(max_length=50)
    # domain = models.EmailField(max_length=30)
    # level = models.CharField(max_length=17)
    type = models.CharField(max_length=3)
    hm = models.CharField(max_length=40)
    sem=models.IntegerField()
    class Meta:
        app_label = 'subject'

class Exposure_Courses(models.Model):
    course_name = models.CharField(max_length=100)
    sem = models.IntegerField(validators=[MaxValueValidator(10)])
    # class Meta:
    #     app_label = 'Exposure_Courses'
    
# domain values 
# ignore = no comparisoon for sub clash
# any other values = compare

class honorminor(models.Model):
    degree_name = models.CharField(max_length=100)
    start_sem  = models.IntegerField(validators=[MaxValueValidator(10)])
    # class Meta:
    #     app_label = 'honorminor'
