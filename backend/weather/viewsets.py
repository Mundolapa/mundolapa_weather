"""Weather station markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from weather.models import Station
from weather.serializers import StationSerializer


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    """Station marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Station.objects.all()
    serializer_class = StationSerializer
