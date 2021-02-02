from django.urls import path
from .views import UserView, PhotoView, VideoView, MusicView

urlpatterns = [
    path('users', UserView.as_view()),
    path('photos/<str:email>', PhotoView.as_view()),
    path('videos/<str:email>', VideoView.as_view()),
    path('audio/<str:email>', MusicView.as_view()),
]
