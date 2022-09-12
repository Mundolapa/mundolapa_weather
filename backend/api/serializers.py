from rest_framework import serializers

from weather.models import Station


class StationPublicSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Station.objects.all())
    # id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
