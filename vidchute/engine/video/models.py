from django.db import models
from authen.models import Profile

class Video(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    image = models.TextField(max_length=12)
    audio = models.TextField(max_length=12)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Playlist(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    avatar = models.TextField(max_length=12, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PlaylistVideo(models.Model):
    playlist = models.OneToOneField(Playlist, on_delete=models.CASCADE)
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    icon = models.TextField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
