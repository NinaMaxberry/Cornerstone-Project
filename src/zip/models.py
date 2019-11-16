from django.db import models

# Create your models here.
class zip(models.Model):
    zip_code = models.IntegerField(default = 0) #can integers be limited?
    county = models.TextField(default = "")
    district = models.IntegerField(default=0)
    

class rep(models.Model):
    f_name = models.TextField()
    l_name = models.TextField()
    

