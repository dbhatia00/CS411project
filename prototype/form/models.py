from django.db import models

# Create your models here.

i=0

class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=32)

def __str__(self):
    return "Search " + str(self.id) + " was: " + self.title