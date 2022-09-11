from django.urls import path

from weather.views import MarkersMapView

app_name = "weather"

urlpatterns = [
    path('map/', MarkersMapView.as_view(), name='map'),
]
