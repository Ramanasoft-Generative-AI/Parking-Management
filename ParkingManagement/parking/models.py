from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    parking_area_no = models.IntegerField()
    vehicle_type = models.CharField(max_length=20,null=False)
    vehicle_limit = models.IntegerField()
    parking_charge = models.DecimalField(max_digits=3, decimal_places=2)
    status = models.BooleanField(default=True)
    doc = models.DateTimeField(default=datetime.now)
    action = models.BooleanField(default=True)

class AddVehicle(models.Model):
    vehicle_no = models.CharField(max_length=200, null=False)
    parking_area_no = models.IntegerField()
    vehicle_type = models.CharField(max_length=200, null=False)
    parking_charge = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)
    arrival_time = models.DateTimeField(default=datetime.now)
    action = models.BooleanField(default=True)
