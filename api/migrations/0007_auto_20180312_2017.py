# Generated by Django 2.0.2 on 2018-03-12 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180312_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensortype', to='api.SensorType'),
        ),
    ]
