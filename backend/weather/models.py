from django.contrib.gis.db import models


class Station(models.Model):
    """A marker for a weather station with name, location, status and optional date fields."""
    name = models.CharField(max_length=255)
    altitude = models.IntegerField()
    location = models.PointField()
    status = models.BooleanField()
    installation_date = models.DateField(null=True, blank=True)
    last_maintenance_date = models.DateField(null=True, blank=True)
    data_start_date = models.DateField(null=True, blank=True)
    data_last_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StationData(models.Model):
    """Weather data for every weather station"""
    station = models.ForeignKey(Station, related_name='stations', on_delete=models.CASCADE)
    temperature_avg = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    temperature_max = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    temperature_min = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    relative_humidity = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    sunshine_duration = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    global_radiation = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    daily_eto = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    wind_speed = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    precipitation = models.DecimalField(
        max_digits=12, decimal_places=5, default=0)
    datetime = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Station: {self.station.name}, Datetime: {self.datetime.astimezone()}'

    @property
    def stations(self):
        return self.station

    class Meta:
        verbose_name_plural = "weather data"
