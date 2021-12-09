from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32)

    def __str__(self):
        return "Hi, " + self.name + " your ID is: " + self.user_id

class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=32)

    def __str__(self):
        return "Search " + str(self.id) + " was: \"" + self.title + "\" by " + self.artist
