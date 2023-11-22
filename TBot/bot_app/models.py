from django.db import models


class Osvencim(models.Model):
    name = models.CharField(max_length=255)
    type_of_execution = models.CharField(max_length=255)
