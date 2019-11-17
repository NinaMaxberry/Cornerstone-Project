from django.db import models

# Create your models here.
class zip(models.Model):
    zip = models.IntegerField(default = 0)
    county = models.TextField(default = "")

    

    
class rep(models.Model):
    zip = models.IntegerField(default = 0)
    f_name = models.TextField()
    l_name = models.TextField()
    


class district(models.Model):
    congressional_district = models.IntegerField(default=0)
    zcta = models.IntegerField(default = 0) #can integers be limited?