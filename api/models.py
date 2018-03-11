from django.contrib.auth.models import User
from django.db import models

# Abstract Model
class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.
class Unit(BaseModel):
    name = models.CharField(max_length=255)


class Local(BaseModel):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, related_name="locals", on_delete=models.CASCADE)
    

class SensorType(BaseModel):
    name = models.CharField(max_length=255)


class Sensor(BaseModel):
    sensor_type = models.ManyToManyField(SensorType)
    local = models.ForeignKey(Local, related_name="sensors", on_delete=models.CASCADE)
    measurement_value = models.FloatField()
    unit_of_measurement = models.CharField(max_length=255)
    modified_at = models.DateTimeField(auto_now=True)


class Alert(BaseModel):
    sensor = models.ForeignKey(Sensor, related_name="alertas", on_delete=models.CASCADE)
    