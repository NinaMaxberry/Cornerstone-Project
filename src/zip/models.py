from django.db import models

# Create your models here.
class zip(models.Model):
    code = models.IntegerField() #can integers be limited
    summary = models.TextField(default = 'Thanks!')