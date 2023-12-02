from datetime import datetime
from django.utils import timezone

from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
