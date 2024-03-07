from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Interest(models.Model):
    interests = models.CharField(max_length=100, unique=True)


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    
    interests = models.ManyToManyField(Interest)
