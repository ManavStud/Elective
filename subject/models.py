from django.db import models
from django.contrib.postgres.fields import ArrayField

class subject(models.Model):
    sub_id= models.CharField(max_length=100, primary_key=True)
    sub_name = models.CharField(max_length=100)
    dept=models.CharField(max_length=50)
    # domain = models.EmailField(max_length=30)
    # level = models.CharField(max_length=17)
    type = models.CharField(max_length=3)
    hm = models.CharField(max_length=40)
    sem=models.IntegerField()

# domain values 
# ignore = no comparisoon for sub clash
# any other values = compare


