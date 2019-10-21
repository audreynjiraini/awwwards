from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    avatar = models.ImageField(upload_to= 'avatars/', null= True, default= 'default.jpg')
    bio = models.TextField()
    
    
    def __str__(self):
        return self.user.username
     
    
    
class Project(models.Model):
    
    title = models.CharField(max_length= 50)
    image = models.ImageField(upload_to= 'projects/')
    description = models.TextField()
    link = models.CharField(max_length= 200)
    author = models.ForeignKey(Profile, on_delete= models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add= True)
    
    
    def __str__(self):
        return self.title
    
    
    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains= search_term)
        return projects
   
    
    
class Contact(models.Model):
    
    # profile = models.OneToOneField(Profile, on_delete= models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE)
    phone_number = PhoneField(blank= False, help_text= 'Contact phone number')
    email = models.EmailField(blank= False)
    github = models.CharField(max_length= 70, null= True)
    
    
    def __str__(self):
        return self.profile.user.username