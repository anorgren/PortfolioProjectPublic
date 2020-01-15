from django.db import models


class Job(models.Model):
    """Creates the model for the jobs app."""
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=255)
