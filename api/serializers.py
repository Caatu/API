from rest_framework import serializers
from api.models import *


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        filds = ('max_temp', 'min_temp', 'sensor')

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('name','created_at')

class SensorMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorMeasure
        fields = ('sensor', 'measurement_value', 'unit_of_measurement', 'modified_at')

class SensorSerializer(serializers.ModelSerializer):
    sensor_type = SensorTypeSerializer()
    class Meta:
        model = Sensor
        fields = ('sensor_type', 'local', 'name', 'modified_at')

class LocalSerializer(serializers.ModelSerializer):
    sensors = SensorSerializer(many=True)

    class Meta:
        model = Local
        fields = ('name', 'sensors')


class UnitSerializer(serializers.ModelSerializer):
    # mudar o nome locals pois ele é reservado 
    locals = LocalSerializer(many=True)

    class Meta:
        model = Unit
        fields = ('name', 'locals')

    def create(self, validated_data):
        locals_data = validated_data.pop('locals')
        unit = Unit.objects.create(**validated_data)
        for local_data in locals_data:
            Local.objects.create(unit=unit, **local_data)
        return unit