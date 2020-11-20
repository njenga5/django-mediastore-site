from django.contrib import admin
from . import models

admin.site.register(models.Photo)
admin.site.register(models.Collection)
admin.site.register(models.Music)
admin.site.register(models.Video)