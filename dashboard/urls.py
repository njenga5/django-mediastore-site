from django.urls import path, re_path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('upload/photo', views.upload_photo, name='upload-photo'),
    path('upload/music', views.upload_music, name='upload-music'),
    path('upload/video', views.upload_video, name='upload-video'),
    path('profile/details', views.profile_details, name='profile-details'),
    path('home', views.dashboard_home, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('edit/find/<str:item>/<int:item_id>', views.find_item, name='find-item'),
    path('edit/photo/<int:pk>', views.edit_photo_view, name='edit-photo'),
    path('edit/delete/<str:item>/<int:item_id>', views.delete_item, name='delete-item'),
]

   