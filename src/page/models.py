from django.db import models


# Create your models here.

class mainData(models.Model):
    Zip = models.IntegerField(primary_key=True)
    district = models.IntegerField()
    CongressDistrict = models.IntegerField()
    First_Name = models.TextField(max_length=50)
    Last_Name = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.Zip}{self.district}{self.CongressDistrict}{self.First_Name}{self.Last_Name}'