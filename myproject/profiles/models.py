from django.db import models

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique = True)
    full_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__ (self):
        return self.username