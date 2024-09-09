from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=500, blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username=models.CharField(max_length=500,blank=True,null=True)
    short_intro= models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField(null=True,blank=True)
    profile_img = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=500, blank=True,null=True)

    social_stackoverflow= models.CharField(max_length=500, blank=True,null=True)
    social_linkedin = models.CharField(max_length=500, blank=True,null=True)
    social_twitter = models.CharField(max_length=500, blank=True,null=True)
    social_website = models.CharField(max_length=500, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.username)
    
    class Meta:
         ordering=['-created']
    
    
      
    @property
    def imageURL(self):
         try:
           url=self.profile_img.url

           
         except:
            url=''
            
        
           
         return url


class skill(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=500, blank=True,null=True)
    descrption=models.TextField(max_length=500, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.name)
    
    
    
class Message(models.Model):
    readed=(('Readed','yes'),('not readed','no'),)
    
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    receipient=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name="messages")
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    subject=models.CharField(max_length=200,null=True,blank=True)
    body=models.TextField()
    is_read=models.BooleanField(default=False,null=False)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    
    def __str__(self):
        return self.subject
    
    class Meta:
        ordering=['is_read','-created',]
    
    
    


    
    
        
    


    
    

    
