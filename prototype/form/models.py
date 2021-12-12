from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    user_id = models.CharField(max_length=32)
    class Meta:
        unique_together = ["name", "user_id"]

    def __str__(self):
        return self.name
        

class Song(models.Model):
    title = models.CharField(max_length=128, unique=True)
    tone = models.CharField(max_length=64)

    def __str__(self):
        return "\"" + self.title + "\""
