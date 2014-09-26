from django.db import models

class Link(models.Model):
    link_name = models.CharField(max_length=255, unique=True)
    link_to = models.URLField(max_length=255)
    