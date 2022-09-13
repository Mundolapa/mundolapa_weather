from django.contrib.gis import admin

from weather.models import Station, StationData
from leaflet.admin import LeafletGeoAdmin


@admin.register(Station)
class StationAdmin(LeafletGeoAdmin):
    list_display = ("name", "location")


@admin.register(StationData)
class StationDataAdmin(admin.ModelAdmin):
    # list_display = ['value', 'when', 'duration', 'sensor_id']
    list_filter = ['event_date']
