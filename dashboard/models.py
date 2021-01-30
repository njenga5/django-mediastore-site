from django.db import models
from PIL import Image
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from commonops.models import User
   

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"))
    tags = TaggableManager()
    # collections = models.ManyToManyField(Collection)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    picture = models.ImageField(upload_to="pictures/")
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.picture.path)


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"))
    tags = TaggableManager()
    # collections = models.ManyToManyField(Collection)
    title = models.CharField(max_length=500)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    video = models.FileField(upload_to="videos/")
    thumbnail = models.ImageField(upload_to='thumbnails/', default='default/Video.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.thumbnail.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.thumbnail.path)

    def __str__(self):
        return self.title


class Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"))
    tags = TaggableManager()
    # collections = models.ManyToManyField(Collection)
    title = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    track = models.FileField(upload_to="music/")
    art = models.ImageField(upload_to='arts/', default='default/screen-0.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.art.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.art.path)

    def __str__(self):
        return self.title


class AlbumDescription(models.Model):
    """
    Gives the title and description for the introductory text in the album.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"))
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
