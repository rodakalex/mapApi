from rest_framework import serializers

from .models import Path


class PathListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
