from django.db.models import Q
from .models import Profile,skill

def searchprofiles(request):
       search=''
       
       if request.GET.get('search'):
              search=request.GET.get('search')
       skills=skill.objects.filter(Q(name__icontains=search))
       pr=Profile.objects.distinct().filter(Q(name__icontains=search)|
                                 Q(short_intro__icontains=search)| 
                                 Q(skill__in=skills))
       
       
       
       return pr,search

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def paginationprofile(request,profiles,results):
       
       page=request.GET.get('page')
       paginator=Paginator(profiles,results)
       try:
         profiles=paginator.page(page)
       except PageNotAnInteger:
           page=1
           profiles=paginator.page(page)
           
       except EmptyPage:
           page=paginator.num_pages
           profiles=paginator.page(page)
           
           
       leftIndex=(int(page)-4)
       if leftIndex<1:
              leftIndex=1
              
       rightIndex=(int(page)+5)
       if rightIndex>paginator.num_pages:
              rightIndex=paginator.num_pages+1
           
       custom_range=range(leftIndex,rightIndex)
       return custom_range, profiles
