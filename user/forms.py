from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile,skill,Message
from project.models import Project
from django import forms

class Customform(UserCreationForm):
       class Meta:
           model=User
           fields=['first_name','email','username','password1','password2']
           labels = {'first_name':'name'}
           
       
       def __init__(self,*args,**kwargs):
              super(Customform,self).__init__(*args,**kwargs)
              
              for name,field in self.fields.items():
                     field.widget.attrs.update({'class':'input'})
                     
class Profileform(ModelForm):
       class Meta:
              model=Profile
              fields="__all__"
              exclude=['user']
       
       def __init__(self,*args,**kwargs):
              super(Profileform,self).__init__(*args,**kwargs)
              
              for name,field in self.fields.items():
                     field.widget.attrs.update({'class':'input'})
                     
class SkillForm(ModelForm):
       class Meta:
              model=skill
              fields=['name','descrption']
                            
       def __init__(self,*args,**kwargs):
              super(SkillForm,self).__init__(*args,**kwargs)
              for name,field in self.fields.items():
                     field.widget.attrs.update({'class':'input'})
              


              
class MessageForm(ModelForm):
      class Meta:
             model=Message
             fields='__all__'
             exclude=['sender','receipient','is_read']
             
      def __init__(self,*args,**kwargs):
              super(MessageForm,self).__init__(*args,**kwargs)
              for name,field in self.fields.items():
                     field.widget.attrs.update({'class':'input'})
       
