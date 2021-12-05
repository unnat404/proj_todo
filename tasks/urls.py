from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='list'),
    path('update_task/<str:pk>/',views.updateTask,name='update_task'), 
    #origianl video me name="update_task" , toh koi issue hoga toh iska change krna here and also in the list.html
    path('delete/<str:pk>/',views.deleteTask,name='delete'),
    ]