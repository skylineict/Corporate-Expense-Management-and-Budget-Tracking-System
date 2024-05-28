from django.urls import path
from .expenses import ExpensVeiw,ExpensesDatailsview

urlpatterns = [
    path("", ExpensVeiw.as_view(), name='expen'),
     path("<int:pk>", ExpensesDatailsview.as_view(), name='expensive'),



   
]