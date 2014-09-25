from django.db import models

class Link(models.Model):
    link_name = models.CharField(max_length=255)
    link_to = models.CharField(max_length=255)
    