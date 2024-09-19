from django.db.models.signals import post_save,post_delete
from .models import User,Profile,skill

from django.core.mail import send_mail
from django.conf import settings

def createdprofile(sender,instance,created,**kwargs):
    print('profile signal trigered')
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        
        subject = "Welcome to Dev Connect!"
    message = f"Hi {user.username},\n\nWelcome to Dev Connect! We are excited to have you join our developer community. Start exploring and connecting with other developers.\n\nBest Regards,\nDev Connect Team"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
            
            
        )
        
        
        
def updateprofile(created,sender,instance,**kwargs):
    profile=instance
    user=profile.user
    
    if created==False:
       user.first_name=profile.name
       user.username=profile.username
       user.email=profile.email
       user.save()
        
       print("created user")
     


def deleteprofile(sender,instance, **kwargs):
    try:
     user=instance.user
     user.delete()
     print('deleted')
     
    except:
        pass
    

     
    
     
post_save.connect(createdprofile, sender=User)
post_delete.connect(deleteprofile, sender=Profile)
post_save.connect(updateprofile,sender=Profile)
    
    

    
