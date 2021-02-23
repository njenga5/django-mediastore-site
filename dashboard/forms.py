from django import forms
from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = [
            'description',
            'picture',
        ]


class MusicForm(forms.ModelForm):
    class Meta:
        model = models.Music
        fields = [
                'artist',
                'title',
                'description',
                'track',
                'art'
        ]


class VideoForm(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = [
                'artist',
                'title',
                'description',
                'video',
                'thumbnail'
        ]


class AlbumDescriptionForm(forms.ModelForm):
    """
    """
    class Meta:
        model = models.AlbumDescription
        fields = [
            'title',
            'description',
        ]