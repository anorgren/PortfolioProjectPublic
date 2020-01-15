from django.db import models


class Blog(models.Model):
    """Creates a Blog model"""
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
