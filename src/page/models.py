from django.db import models

# Create your models here.
class zip(models.Model):
    zip = models.IntegerField(default = 0, primary_key=True)
    county = models.TextField(default = "")

    

    def __str__(self):
        return f'{self.zip} {self.county}'

class rep(models.Model):
    zip = models.IntegerField(default = 0, primary_key=True  )
    f_name = models.TextField()
    l_name = models.TextField()

    def __str__(self):
        return f'{self.f_name} {self.l_name}'
    
class district(models.Model):
    congressional_district = models.IntegerField(default=0)
    zcta = models.IntegerField(default = 0, primary_key=True) #can integers be limited like Charfields?

    
    def __str__(self):
        return f'{self.congressional_district} {self.zcta}'

