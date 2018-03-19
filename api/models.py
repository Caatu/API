from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import reciver

# Abstract Model
class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.name

    class Meta:
        abstract = True


# Create your models here.
class Unit(BaseModel):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="units", on_delete=models.CASCADE)
    
#mudar o nome Local pois locals é reservado
class Local(BaseModel):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, related_name="locals", on_delete=models.CASCADE)
    

class SensorType(BaseModel):
    name = models.CharField(max_length=255)


class Sensor(BaseModel):
    name = models.CharField(max_length=255)
    sensor_type = models.OneToOneField(SensorType, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, related_name="sensors", on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

class SensorMeasure(BaseModel):
    sensor = models.ForeignKey(Sensor, related_name="measurements", on_delete=models.CASCADE)
    measurement_value = models.FloatField()
    unit_of_measurement = models.CharField(max_length=255)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.measurement_value) + " " + str(self.unit_of_measurement)


class Alert(BaseModel):
    name = models.CharField(max_length=255)
    max_temp = models.CharField(max_length=255)
    min_temp = models.CharField(max_length=255)
    sensor = models.ForeignKey(Sensor, related_name="alertas", on_delete=models.CASCADE)