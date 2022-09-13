from django.urls import path, include

from weather.views import MarkersMapView, StationDataListView, StationDataDetailAPIView

app_name = "weather"

urlpatterns = [
    path('', include('weather.api')),
    path('map/', MarkersMapView.as_view(), name='map'),
    path('api/', StationDataListView.as_view(),
         name='stationdata-list'),
    path('api/<int:pk>/', StationDataDetailAPIView.as_view(),
         name='sensordata-detail'),
]
