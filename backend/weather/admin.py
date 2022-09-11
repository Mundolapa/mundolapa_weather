from django.contrib.gis import admin

from weather.models import Station
from leaflet.admin import LeafletGeoAdmin


@admin.register(Station)
class StationAdmin(LeafletGeoAdmin):
    list_display = ("name", "location")
