from email.message import Message
from django.shortcuts import render,redirect,get_object_or_404

from .models import Profile,skill
from project.models import Project
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Customform,Profileform,SkillForm,MessageForm
from .models import skill,Message
from django.db.models import Q
from .utils import searchprofiles,paginationprofile



@login_required(login_url="login")

# Create your views here.
def profile(request):
       user=request.user
       profiles,search=searchprofiles(request)
       custom_range,profiles=paginationprofile(request,profiles,3 )
       skills = skill.objects.all()  # Querying all skills
       
       profile=request.user.profile
       messagerequest=profile.messages.all()
       unreadcount=messagerequest.filter(is_read=False).count()

       
       
       context={'profiles':profiles,'search':search,'skills':skills,'range':custom_range,'count':unreadcount,'user':user}
       return render(request,'user/profile.html',context)


def userprofile(request,pk):
       pr=Profile.objects.get(id=pk)
       skills=pr.skill_set.exclude(descrption='')
       other_skill=pr.skill_set.filter(descrption='')
       context={'pr':pr,'skill':skills,'other':other_skill,}


       return render(request,'user/user-profile.html',context)
  

def loginpage(request):
       if request.user.is_authenticated:
              return redirect('profile')
       
       if request.method=='POST':
              username=request.POST['username'].lower()
              password=request.POST['password']
              
              try:
                user= User.objects.get(username=username)
              except:
              
                     messages.error(request,'username not exist')
                     
              user=authenticate(request,username=username,password=password)
              
              if user is not None:
                     login(request,user)
                     if 'next' in request.GET:
                       return redirect(request.GET['next'])
                     else:
                       return redirect('account')

                        
                 
              else:
                 messages.error(request,'username or password was incorrect')                
       return render(request,'user/login_register.html')  

def logoutuser(request):
       logout(request)
       return redirect('login')


def registeruser(request):
     page='register'
     form=Customform()
     if request.method=='POST':
            form=Customform(request.POST)
            if form.is_valid():
                   user=form.save(commit=False)
                   user.username=user.username.lower()
                   user.save()
                   
                   messages.success(request,"user account created")
                   login(request,user)
                   return redirect('edit-account')
            else:
                   
              messages.success(request,"error during account creation ")

              
            
     
     context={'page':page,'form':form}
     return render(request,'user/login_register.html',context)


@login_required(login_url='login')
def useraccount(request):
       pro=request.user.profile
       skills=pro.skill_set.all()
       projects=pro.projects.all()       
       

       context={"pro":pro,"skill":skills,"project":projects}
       return render(request,'user/account.html',context)

@login_required(login_url='login')
def editAccount(request):
       
       pro=request.user.profile
       forms=Profileform(instance=pro)
       if request.method=='POST':
          forms=Profileform(request.POST,request.FILES,instance=pro)
          
          if forms.is_valid():
                project=forms.save(commit=False)
                project.owner=profile
                project.save()
                messages.success(request,'profile updated successfully')
                return redirect("account")         
       context={'form':forms,'pro':pro}

              
       return render(request,'user/profile_form.html',context)



@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'user/skill_form.html', context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'user/skill_form.html', context)

def deleteSkill(request,pk):
       profile=request.user.profile
       skill=profile.skill_set.get(id=pk)
       
       if request.method=="POST":
              skill.delete()
              messages.success(request,"Skill Deleted Successfully")
              return redirect('account')
       context={'object':skill}
       return render(request,'user/delete_template.html',context)
              
              

@login_required(login_url='login')
def inbox(request):
       profile=request.user.profile
       messagerequest=profile.messages.all()
       unreadcount=messagerequest.filter(is_read=False).count()
       context={'message':messagerequest,'count':unreadcount}
       return render(request,'user/inbox.html',context)

@login_required(login_url='login')
def viewmessage(request,pk):
       profile=request.user.profile
       message=profile.messages.get(id=pk)
       
       if message.is_read==False:
         message.is_read=True
         
         message.save()
       context={'message':message,}
       return render(request,'user/message.html',context)

def messageform(request,pk):
       form=MessageForm()
       
       try:
         sender=request.user.profile
       
       except:
         sender=None
        
      
       
       receipient=Profile.objects.get(id=pk)

       
       if request.method=='POST':
              form=MessageForm(request.POST)
              if form.is_valid():
                     

                     message=form.save(commit=False)
       
                     message.sender=sender
                     message.receipient=receipient
                     
                     if sender:
                            message.name=sender.name
                            message.email=sender.email
                            
                              
                     message.save()
                     
                     messages.success(request,"messeage Sended Successfully")
                     return redirect('user-profile',pk=receipient.id)
                     
                     
       
       
       context={"form":form,'receipient':receipient}
       return render(request,'user/messageform.html',context)
       


              
 
