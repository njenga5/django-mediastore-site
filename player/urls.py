from django.urls import path
from . import views


app_name = 'player'

urlpatterns = [
    path('play/audio/', views.play_audio_view, name="play-audio"),
]

