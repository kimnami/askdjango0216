from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20, blank=True)
    content = models.TextField()