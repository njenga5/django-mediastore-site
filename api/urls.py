from django.urls import path
from .views import UserView, PhotosView, VideosView, MusicsView, SinglePhotoView

urlpatterns = [
    path('users', UserView.as_view()),
    path('photos/<str:email>', PhotosView.as_view()),
    path('videos/<str:email>', VideosView.as_view()),
    path('audio/<str:email>', MusicsView.as_view()),
    path('photo/edit/<int:pk>', SinglePhotoView.as_view()),
]
