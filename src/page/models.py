from django.db import models

# Create your models here.
class Zipcodes(models.Model):
    zip = models.IntegerField(default = 0, primary_key=True)
    county = models.TextField(default = "")

    def __str__(self):
        return f'{self.zip} {self.county}'

class Rep(models.Model):
    zip = models.IntegerField(default = 0, primary_key=True  )
    f_name = models.TextField()
    l_name = models.TextField()

    def __str__(self):
        return f'{self.f_name} {self.l_name}'
    
class District(models.Model):
    congressional_district = models.IntegerField(default=0)
    zip = models.IntegerField(default = 0, primary_key=True) #can integers be limited like Charfields?

    def __str__(self):
        return f'{self.congressional_district} {self.zip}'



    
    

