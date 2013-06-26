from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    name = models.CharField(max_length=140)
    user = models.ForeignKey(User)