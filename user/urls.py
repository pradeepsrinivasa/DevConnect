from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('',views.profile,name='profile'),
    path('profile/<str:pk>',views.userprofile,name='user-profile'),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('register',views.registeruser,name='register'),
    path('account',views.useraccount,name='account'),
    path('Edit-account',views.editAccount,name='edit-account'),
    path('skills',views.createSkill,name='skill'),
    path('update_skill/<str:pk>',views.updateSkill,name='updateskill'),
    path('delete_skill/<str:pk>',views.deleteSkill,name='deleteskill'),
    
    path('inbox/',views.inbox,name='inbox'),
    path('message/<str:pk>/',views.viewmessage,name='message'),
    path('messageform/<str:pk>/',views.messageform,name='message-form')

    
    








    ]