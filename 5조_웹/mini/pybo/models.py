from django.db import models

class images(models.Model):
    name = models.CharField(max_length=30)
    image_urls = models.CharField(max_length=200)
    images = models.TextField()
    image_paths = models.TextField(null=True)