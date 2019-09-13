from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    cover_image = models.URLField()

    def __str__(self):
        return f"{self.user.username}-{self.title}"
