from django.urls import path
from .create_list import create_todolist
from .create_list import Listandcreateview





urlpatterns = [
   
    path("create", create_todolist, name='listview'),
     path("todolist", Listandcreateview.as_view(), name='list'),
    
   
]