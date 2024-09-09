from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework.response import Response
from .serializers import ProjectSerializer,ProfileSerializer
from project.models import Project,review,Tag
from user.models import Profile

@api_view(['GET'])
def getRoutes(request):
       
       routes=[
              {'GET':'/api/projects'},
              {'GET':'/api/projects/id'},
              {'POST':'/api/projects/id/vote'},
              
              {'POST':'/api/user/token'},
              {'POST':'/api/user/token/refresh'}
          
       ]

       
       return Response(routes)
       
@api_view(['GET'])
def getProjects(request):
       print('User:',request.user)
       projects=Project.objects.all()
       serializer=ProjectSerializer(projects,many=True)
       return Response(serializer.data)

@api_view(['GET'])
def getProject(request,pk):
       projects=Project.objects.get(id=pk)
       serializer=ProjectSerializer(projects,many=False)
       return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectview(request,pk):
       user=request.user.profile
       project=Project.objects.get(id=pk)
       data=request.data
       
       reviews,created= review.objects.get_or_create(
              owner=user,
              project=project
              
       )
       
       reviews.value=data['value']
       reviews.save()
       project.getVoteCount
       
       
       serializer=ProjectSerializer(project,many=False)
       return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def profileview(request,pk):
       profile=Profile.objects.get(id=pk)
       Data=request.data
       profile.short_intro=Data["value"]
       profile.save()
       serializer=ProfileSerializer(profile,many=False)
       return Response(serializer.data)
            
            
            
@api_view(['DELETE'])
def removeTag(request):
       tag_id=request.data['tag']
       projectId=request.data['project']
       
       
       project=Project.objects.get(id=projectId)
       tag=Tag.objects.get(id=tag_id)
       
       project.tag.remove(tag)
       return Response("Tag was deleted!")