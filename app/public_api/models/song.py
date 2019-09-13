from django.db import models
from .album import Album


class Song(models.Model):
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"{self.album.title}-{self.name}"
