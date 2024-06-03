from django.urls import path
from .loginview import GoogleloginVeiw,Facebookclassview


urlpatterns = [
   
    path('google', GoogleloginVeiw.as_view(), name='google'),
    path('facebook', Facebookclassview.as_view(), name='facebook')

    
   
   
]