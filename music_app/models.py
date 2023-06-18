from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# class User(AbstractUser):
    # email=models.EmailField(unique=True)

class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]
    title=models.CharField(max_length=100)
    music_file=models.FileField(upload_to='music/')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default=PUBLIC)
    allowed_users = models.ManyToManyField(User, related_name='allowed_files', blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)