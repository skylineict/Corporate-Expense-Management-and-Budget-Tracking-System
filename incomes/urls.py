from django.urls import path
from .incomeview import ListincomeView,UpdateIncome


urlpatterns = [

    path("", ListincomeView.as_view(), name='listincome'),
    path("<int:pk>", UpdateIncome.as_view(), name='income'),
    
  
    #  path("<int:pk>", ExpensesDatailsview.as_view(), name='expensive'),



   
]