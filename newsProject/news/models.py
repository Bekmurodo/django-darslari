from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    #author = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.title