from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=128)
    tone = models.CharField(max_length=64)

    def __str__(self):
        return "\"" + self.title + "\""
