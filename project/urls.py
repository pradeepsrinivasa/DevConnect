from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/<str:pk>',views.project,name='project'),
    path('',views.projects,name='projects'),
    path('create_form',views.CreateProject,name='create_form'),
    path('update_form/<str:pk>/',views.UpdateProject,name='update_form'),
    path('delete-project/<str:pk>/',views.deleteProject,name='delete-project'),
    path('delete_project/<str:pk>',views.deleteProject,name='deleteproject'),
    path('create_project',views.CreateProject,name='createproject'),
    path('update_project/<str:pk>',views.UpdateProject,name='updateproject'),
    path('health/', health_check, name='health_check'),




 
]   
