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
                'title',
                'description',
                'track',
        ]


class VideoForm(forms.ModelForm):
    class Meta:
        model = models.Video
        fields = [
                'title',
                'description',
                'video',
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