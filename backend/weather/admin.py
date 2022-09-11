from django.contrib.gis import admin

from weather.models import Station


@admin.register(Station)
class StationAdmin(admin.OSMGeoAdmin):
    list_display = ("name", "location")
