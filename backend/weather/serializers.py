from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer

from api.serializers import StationPublicSerializer

from weather.models import Station, StationData


class StationSerializer(GeoFeatureModelSerializer):
    """Weather station marker GeoJSON serializer"""

    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Station


class StationDataSerializer(ModelSerializer):
    station = StationPublicSerializer()

    class Meta:
        model = StationData
        fields = [
            'id',
            'temperature_avg',
            'temperature_max',
            'temperature_min',
            'relative_humidity',
            'sunshine_duration',
            'global_radiation',
            'daily_eto',
            'wind_speed',
            'precipitation',
            'datetime',
            'station',
        ]

