from django.views.generic.base import TemplateView
from rest_framework import generics

from weather.models import StationData

from . import serializers


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "weather/map.html"


class StationDataListView(generics.ListAPIView):
    queryset = StationData.objects.all()
    serializer_class = serializers.StationDataSerializer


class StationDataDetailAPIView(generics.RetrieveAPIView):
    queryset = StationData.objects.all()
    serializer_class = serializers.StationDataSerializer
