from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('upload/photo/', views.upload_photo, name='upload-photo'),
    path('upload/music/', views.upload_music, name='upload-music'),
    path('upload/video/', views.upload_video, name='upload-video'),
    path('profile/details/', views.profile_details, name='profile-details'),
    path('', views.dashboard_home, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('change/delete/<str:item>/<int:item_id>/', views.delete_item, name='delete-item'),
    path('collection/add/<int:item_id>/<str:source>/', views.add_to_collection, name='add-to-collection'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
