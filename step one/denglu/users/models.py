from django.db import models

# Create your models here.
from django.db import models
import uuid


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.UUIDField(default=uuid.uuid4)
