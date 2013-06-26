from django.db import models
from django.contrib.auth import User

class Videos(models.Model):
    name = models.CharField(max_length=140)
    user = models.ForeignKey(User)