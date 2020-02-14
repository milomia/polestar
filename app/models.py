from django.db import models

# Create your models here.
class Position(models.Model):
    imo_number = models.IntegerField(unique=False)
    timestamp = models.DateTimeField()
    latitude =  models.FloatField()
    longitude = models.FloatField() 

class Ship(models.Model):
    imo_number = models.IntegerField(unique=False)
    name = models.CharField(max_length=30)
