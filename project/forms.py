from django.forms import ModelForm
from .models  import Project,review
from django import forms


class CreateProjectForm(ModelForm):
       class Meta:
              model=Project
              fields= ['title','description','demo_link','source_link','featured_img']
              widgets={
                  'tag':forms.CheckboxSelectMultiple()

              }
              
       
       def __init__(self,*args,**kwargs):
              super(CreateProjectForm,self).__init__(*args,**kwargs)
              for name,field in self.fields.items():
                     field.widget.attrs.update({'class':'input'})


              #self.fields['title'].widget.attrs.update({'class':'input','placeholder':'select'})
              
class ReviewForm(ModelForm):
       class Meta:
         model=review
         fields='__all__'
         exclude=('owner','project')
         labels={
                'value':'Place Your Vote',
                'body':'Add your comment about Project'
         }
       
       
       def __init__(self, *args, **kwargs):
              super(ReviewForm,self).__init__(*args,*kwargs)

              for name, field in self.fields.items():
                     field.widget.attrs.update({'class':'input'})
       

