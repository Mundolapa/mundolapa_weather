"""Station markers API URL Configuration."""

from rest_framework import routers

from weather.viewsets import StationViewSet

router = routers.DefaultRouter()
router.register(r"markers", StationViewSet)

urlpatterns = router.urls
