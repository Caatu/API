from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Alert, Local, Sensor, Unit
from api.serializers import *
from api.serializers import UserSerializer


class UserCreate(APIView):
    """ 
    Creates the user. 
    """
    permission_classes = ()

    def post(self, request, format='json'):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuth(APIView):

    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            token_informations = Token.objects.get_or_create(user=user)
            TOKEN_ACCESS_INDEX = 0
            token = token_informations[TOKEN_ACCESS_INDEX]

            response = {
                'id': user.id,
                'username': user.username,
                'token': token.key,
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response("Credenciais Inválidas", status=status.HTTP_400_BAD_REQUEST)



class UnitsUser(APIView):
    permission_classes = ()

    def get(self, request, pk):
        queryset = Unit.objects.filter(user=pk)
        serializer = UnitSerializer(queryset, many = true)
        return Response(serializer.data)

class UnitsView(APIView):

    permission_classes = ()

    def get(self, request):
        queryset = Unit.objects.all()
        serializer = UnitSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.get("id"), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnitDetailsView(APIView):
    permission_classes = ()

    def get(self, request, pk):

        try:
            unit = Unit.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"error": "Unidade não encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UnitSerializer(unit)

        return Response(serializer.data)
        

    def delete(self, request, pk):
        try:
            Unit.objects.delete(pk=pk)
        except ObjectDoesNotExist:
            return Response({"error": "Erro ao apagar, unidade não encontrada!"}, status=status.HTTP_404_NOT_FOUND)

    
    def update(self, request, pk):
        unit = Unit.objects.filter(id=pk)
        if unit is not None:
            unit.name = request.data.get("name")
            unit.save()
            return Response("Editado com sucesso!",status=status.HTTP_200_OK)
        else:
            return Response("Falha ao editar, unidade não encontrada!", status=status.HTTP_400_BAD_REQUEST)


class LocalsViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.values('name', 'colectors')
    serializer_class = LocalSerializer
    authentication_classes = []
    permission_classes = ()


class ColectorsViewSet(viewsets.ModelViewSet):
    queryset = Colector.objects.all()
    serializer_class = ColectorSerializer
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
