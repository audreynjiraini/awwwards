from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatars/', null = True, default = 'default.jpg')
    bio = models.TextField()
    
    
    def __str__(self):
        return self.user.username
    
    
    
class Project(models.Model):
    
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/')
    description = models.TextField()
    link = models.CharField(max_length = 200)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.title