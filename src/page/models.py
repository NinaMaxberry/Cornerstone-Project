from django.db import models 




# Create your models here.

class KentuckyProject(models.Model):
    Zip = models.IntegerField()
    District = models.IntegerField()
    CongressDistrict = models.TextField()
    First_Name = models.TextField()
    Last_Name = models.TextField ()
    Message = models.TextField()

    

    def __str__(self):
        return f'{self.Zip} {self.District} {self.CongressDistrict} {self.First_Name} {self.Last_Name} {self.Message}'
    

class Csv(models.Model):
    zip = models.IntegerField()
    primary_city = models.TextField()
    county = models.TextField()
    area_codes = models.CharField(max_length=5)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.zip} {self.primary_city} {self.county} {self.area_codes} {self.message}'

