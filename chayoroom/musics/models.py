from django.db import models


class new_add(models.Model):
    name = models.CharField(max_length=255)
    genere = models.CharField(max_length=255)
    music_url = models.CharField(max_length=2083)
