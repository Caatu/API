from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Unit, Local, Sensor, Alert
# Create your views here.


@csrf_exempt
def units_list(request):
    if request.method == 'POST':
        units = Unit.objects.all()


@csrf_exempt
def locals_list(request):
    if request.method == 'POST':
        locals = Local.objects.all()


@csrf_exempt
def sensors_list(request):
    if request.method == 'POST':
        sensors = Sensor.objects.all()


@csrf_exempt
def alerts_list(request):
    if request.method == 'POST':
        alerts = Alert.objects.all()