# Generated by Django 4.0.7 on 2022-09-12 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_weatherdata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeatherData',
            new_name='StationData',
        ),
    ]
