from django.db import models
from django.utils import timezone
 

class Board(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
	     return self.title

class Post(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    belong = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='boards')

    def __str__(self):
	     return self.text





  


