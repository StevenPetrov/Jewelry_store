from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image_field = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username