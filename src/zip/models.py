from django.db import models

# Create your models here.
class zip(models.Model):
    code = models.IntegerField() #can integers be limited?
    county = models.TextField(default = "")
    district = models.IntegerField(default=0)
    name = models.TextField(blank=True)
    

