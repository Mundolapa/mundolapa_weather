from dataclasses import field
from msilib.schema import Class
from rest_framework_gis import serializers

from weather.models import Station


class StationSerializer(serializers.GeoFeatureModelSerializer):
    """Weather station marker GeoJSON serializer"""

    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Station