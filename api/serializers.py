from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import *


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=6, max_length=100,
                                     write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        filds = ('id', 'max_temp', 'min_temp',
                 'sensor', 'created_at', 'modified_at')


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('id', 'created_at')


class SensorMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorMeasure
        fields = ('id', 'sensor', 'measurement_value',
                  'unit_of_measurement', 'modified_at')


class SensorSerializer(serializers.ModelSerializer):
    sensor_type = SensorTypeSerializer()

    class Meta:
        model = Sensor
        fields = ('id', 'sensor_type',
                  'name', 'modified_at', 'created_at')


class ColectorSerializer(serializers.ModelSerializer):
    sensors = SensorSerializer(many=True)

    class Meta:
        model = Colector
        field = ('id', 'identify', 'local')


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('id', 'name', 'sensors', 'created_at')


class LocalSerializerWithoutSensors(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('id', 'name', 'created_at')


class UnitSerializer(serializers.ModelSerializer):
    # mudar o nome locals pois ele é reservado
    locals = LocalSerializerWithoutSensors(many=True)
    def create(self, validated_data):
        unit = Unit.objects.create(user_id = validated_data('user_id'), name = validated_data('name'))
        unit.save()
        return unit

    class Meta:
        model = Unit
        fields = ('id', 'name', 'locals', 'created_at')
    

