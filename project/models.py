from django.db import models
import uuid
from user.models import Profile
# Create your models here.


class Project(models.Model):
       owner= models.ForeignKey(Profile,null=True,on_delete=models.CASCADE,related_name='projects')
       title=models.CharField(max_length=200)
       description=models.TextField(null=True,blank=True)
       id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
       demo_link=models.CharField(null=True,blank=True,max_length=200)
       source_link=models.CharField(null=True,blank=True,max_length=200)
       created=models.DateTimeField(auto_now_add=True)
       featured_img=models.ImageField(null=True,blank=True,default="default.img")
       tag=models.ManyToManyField('Tag',blank=True)
       vote_total=models.IntegerField(default=0,blank=True,null=True)
       vote_ratios=models.IntegerField(default=0,blank=True,null=True)



       def __str__(self):
         return self.title
  
       class Meta:
         ordering=['-vote_total','title']
         
       
       @property
       def imageURL(self):
         try:
           url=self.featured_img.url

           
         except:
            url=''
            
        
           
         return url
 
       @property
       def reviewers(self):
              query_set=self.review_set.all().values_list('owner__id',flat=True)
              return query_set
         
       @property
       def getVoteCount(self):
              reviews=self.review_set.all()
              upVotes=reviews.filter(value='up').count()
              totalvotes=reviews.count()
              ratio=(upVotes/totalvotes)*100
              self.vote_total=totalvotes
              self.vote_ratios=ratio
              self.save()
              
       

class review(models.Model):
       vote_type=(("up","Up Vote"),("down","Down Up"),)
       owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
       
       project=models.ForeignKey(Project,on_delete=models.CASCADE)
       value=models.CharField(max_length=200,choices=vote_type,default=('up','Up Vote'))
       
       body=models.TextField(null=True,blank=True,max_length=200)
       created=models.DateTimeField(auto_now_add=True)
       id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
       
       class Meta:
              unique_together=[['owner','project']]
       



       def __str__(self):
              return self.value
       
class Tag(models.Model):
       name=models.CharField(max_length=200)
       created=models.DateTimeField(auto_now_add=True)
       id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

       def __str__(self):
              return self.name
       
