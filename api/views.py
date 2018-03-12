from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Unit, Local, Sensor, Alert
from rest_framework import viewsets
from api.serializers import *
# Create your views here.

class UnitsViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    authentication_classes = []
    permission_classes = ()

class LocalsViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    authentication_classes = []
    permission_classes = ()

class SensorsViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    authentication_classes = []
    permission_classes = ()

class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    authentication_classes = []
    permission_classes = ()

class SensorMeasureViewSet(viewsets.ModelViewSet):
    queryset = SensorMeasure.objects.all()
    serializer_class = SensorMeasureSerializer
    authentication_classes = []
    permission_classes = ()

class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    authentication_classes = []
    permission_classes = ()
    