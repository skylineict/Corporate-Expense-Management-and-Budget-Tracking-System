from django.urls import path
from .categories import CategoryDetialsVeiw, CategoryView



urlpatterns = [
  
   path("", CategoryView.as_view(), name='category'),
   path("category/<int:pk>", CategoryDetialsVeiw.as_view(), name='categoryview'),


   
]