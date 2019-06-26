from django.db import models
from django.utils import timezone

# Create your models here.


class country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.country


class customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    order = models.CharField(max_length=255)
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
