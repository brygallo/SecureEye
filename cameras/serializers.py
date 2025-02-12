from rest_framework import serializers
from .models import Camera

class CameraSerializer(serializers.ModelSerializer):
    """
    Serializer for Camera model.
    """
    class Meta:
        model = Camera
        fields = "__all__"
