from django.shortcuts import render,redirect
from .forms import CreateProjectForm,ReviewForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project,Tag,review
from django.db.models import Q
from django.contrib.auth.models import User
from user.models import Profile
from .utils import SearchProject,paginationprojects
from django.contrib import messages



# Create your views here.
def project(request,pk):
       
       projobj=Project.objects.get(id=pk)
       
       form=ReviewForm()
       if request.method=='POST':
              form=ReviewForm(request.POST)
              reviews=form.save(commit=False)
              reviews.project=projobj
              reviews.owner=request.user.profile
              
              reviews.save()
              
              projobj.getVoteCount
              messages.success(request,'review was success submited')
              return redirect('project',pk=pk)
              
              

       page= Project.objects.get(id=pk)
       count=page.tag.all().count()
       print('count:',count)
       r=range(0,4)
       print(r)

       return render(request, 'project/single-project.html',{'project': page,'form':form,'count':r})


def projects(request):
       search,pro=SearchProject(request)
       custom_range,pro=paginationprojects(request,pro,4)
       
      
       return render(request, 'project/projects.html',{'pro':pro,"range":custom_range,'search':search})


              
def deleteProject(request,pk):
       profile=request.user.profile
       project=profile.projects.get(id=pk)
       
       if request.method=="POST":
              project.delete()
              messages.success(request,"Project Deleted Successfully")
              return redirect('account')
       context={'object':project}
       return render(request,'project/delete_template.html',context)

def CreateProject(request):
       profile=request.user.profile
       
       form=CreateProjectForm()
       if request.method=="POST":
              newtags=request.POST.get('newtags').replace(','," ").split()

              form=CreateProjectForm(request.POST,request.FILES)
              if form.is_valid():
                     project=form.save(commit=False)
                     project.owner=profile
                     project.save()
                     
                     for tag in newtags:
                            tag,created=Tag.objects.get_or_create(name=tag)
                            project.tag.add(tag)
                     
                     return redirect('account')
       context={'form':form}
       return render(request,'project/project_form.html',context)

def UpdateProject(request,pk):
       profile=request.user.profile
       project=profile.projects.get(id=pk)
       form=CreateProjectForm(instance=project)
       if request.method=="POST":
              newtags=request.POST.get('newtags').replace(','," ").split()
              form=CreateProjectForm(request.POST,request.FILES,instance=project)
              if form.is_valid():
                     
                     project=form.save()
                     for tag in newtags:
                            tag,created=Tag.objects.get_or_create(name=tag)
                            project.tag.add(tag)
                     return redirect('account')
       context={'form':form,'project':project}
       return render(request,'project/project_form.html',context)


from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", content_type="text/plain")
       
       

       
              
 




