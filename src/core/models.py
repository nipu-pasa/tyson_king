from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

user=get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg=models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    caption=models.ImageField(upload_to='post_images')
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class FollowersCount(models.Model):
    followers=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user
    
    
