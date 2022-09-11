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
