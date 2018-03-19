# Generated by Django 2.0.2 on 2018-03-12 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('max_temp', models.CharField(max_length=255)),
                ('min_temp', models.CharField(max_length=255)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alertas', to='api.Sensor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]