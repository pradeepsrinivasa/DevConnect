from rest_framework import serializers
from project.models import Project,Tag,review
from user.models import Profile    


class ProfileSerializer(serializers.ModelSerializer):
       class Meta:
              model=Profile
              fields='__all__'
              
              
class TagSerializer(serializers.ModelSerializer):
       class Meta:
              model=Tag
              fields='__all__'
              
class ReviewSerializer(serializers.ModelSerializer):
       
       class Meta:
              model=review
              fields='__all__'
              



class ProjectSerializer(serializers.ModelSerializer):
       owner= ProfileSerializer(many=False)
       tag=TagSerializer(many=False)
       reviews=serializers.SerializerMethodField()
       class Meta:
              model=Project
              fields='__all__'
              
       def get_reviews(self,obj):
              reviews=obj.review_set.all()
              serializer=ReviewSerializer(reviews,many=True)
              return serializer.data
              


              

