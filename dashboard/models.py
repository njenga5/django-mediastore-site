from django.db import models
from commonops.models import User


class Collection(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
   

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    collections = models.ManyToManyField(Collection)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    picture = models.ImageField(upload_to="pictures/")


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    collections = models.ManyToManyField(Collection)
    title = models.CharField(max_length=500)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    video = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title


class Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    collections = models.ManyToManyField(Collection)
    title = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    track = models.FileField(upload_to="music/")

    def __str__(self):
        return self.title