from rest_framework import serializers
from api.models import Unit, Local, SensorType, Sensor, Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        filds = ('max_temp', 'min_temp', 'sensor')


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('sensor_type', 'local', 'measurement_value', 'unit_of_measurement', 'modified_at')


class LocalSerializer(serializers.ModelSerializer):
    sensors = SensorSerializer(many=true)

    class Meta:
        model = Local
        fields = ('name', 'sensors')

    def create(self, validated_data):
        sensors_data = validated_data.pop('sensors')
        local = Local.objects.create(**validated_data)
        for sensor_data in sensors_data:
            Sensor.objects.create(local=local, **sensor_data)
        return local


class UnitSerializer(serializers.ModelSerializer):
    # mudar o nome locals pois ele é reservado 
    locals = LocalSerializer(many=true)

    class Meta:
        model = Unit
        fields = ('name', 'locals')

    def create(self, validated_data):
        locals_data - validated_data.pop('locals')
        unit = Unit.objects.create(**validated_data)
        for local_data in locals_data:
            Local.objects.create(unit=unit, **local_data)
        return unit