from django.db import models

# Create your models here.

class News(models.Model):
    sourceURL = models.TextField()
    newsContent = models.TextField()
