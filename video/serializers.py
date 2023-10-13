from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # read_only_fields = ("id")
        fields = ["video", "slug"]