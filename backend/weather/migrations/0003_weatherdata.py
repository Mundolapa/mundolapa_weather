# Generated by Django 4.0.7 on 2022-09-12 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_rename_weatherstation_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_avg', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('temperature_max', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('temperature_min', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('relative_humidity', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('sunshine_duration', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('global_radiation', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('daily_eto', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('wind_speed', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('precipitation', models.DecimalField(decimal_places=5, default=0, max_digits=12)),
                ('datetime', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='weather.station')),
            ],
            options={
                'verbose_name_plural': 'weather data',
            },
        ),
    ]
