from django.db import models
from django.contrib.auth.models import User

from app.storage_backends import PrivateMediaStorage


class Album(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    cover_image = models.URLField()

    def __str__(self):
        return f"{self.user.username}-{self.title}"


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class PrivateDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=PrivateMediaStorage())
    signature_version = "s3v4"
