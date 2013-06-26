from django.db import models

class Videos(models.Model):
    name = models.CharField(max_length=140)