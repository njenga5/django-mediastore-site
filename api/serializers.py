from rest_framework import serializers
from commonops.models import CustomUser as User
from dashboard import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = '__all__'
