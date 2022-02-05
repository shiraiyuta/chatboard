from django.db import models
from django.utils import timezone
 


class Post(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)


class Board(models.Model):
    title = title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now) 


