from .models import Project,Tag
from user.models import Profile
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db .models import Q

def paginationprojects(request,pro,results):
       
       page=request.GET.get('page')
       results = 3
       paginator=Paginator(pro,results)
       
       try:
         pro=paginator.page(page)
         
       except PageNotAnInteger:
           page=1
           pro=paginator.page(page)
           
       except EmptyPage:
           page=paginator.num_pages
           pro=paginator.page(page)
           
           
       leftIndex=(int(page)-4)
       if leftIndex<1:
              leftIndex=1
              
       rightIndex=(int(page)+5)
       if rightIndex>paginator.num_pages:
              rightIndex=paginator.num_pages+1
           
       custom_range=range(leftIndex,rightIndex)
       return custom_range,pro


def SearchProject(request):
       search=''
       
       if request.GET.get('search'):
              search=request.GET.get('search')
              
       
       owners=Profile.objects.filter(user__first_name__icontains=search)
       tags=Tag.objects.filter(name__icontains=search)
       pro=Project.objects.distinct().filter(Q(title__icontains=search)|Q(tag__in=tags)|Q(owner__in=owners))
       return search,pro