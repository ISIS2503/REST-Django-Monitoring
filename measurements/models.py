from django.db import models

# Create your models here.
class Measurement(models.Model):
    measurement = models.CharField(max_length=50)
    value = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    time = models.TimeField(auto_now_add=False)