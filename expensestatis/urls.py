from django.urls import path
from .expenes_search import ExpensesSearchVeiw
from .userexpense import ExpensesUserList,AllUserExpenses,ExpensUserView



urlpatterns = [
    path("", ExpensesSearchVeiw.as_view(), name='search'),
    path('expenseslist/<int:user_id>/',ExpensesUserList.as_view(), name='expense_list'),
    path('totalexpenses/',AllUserExpenses.as_view(), name='allexpenses'),
    path('userexpense/',ExpensUserView.as_view(), name='allexpenses')
    #  path("<int:pk>", ExpensesDatailsview.as_view(), name='expensive'),



   
]