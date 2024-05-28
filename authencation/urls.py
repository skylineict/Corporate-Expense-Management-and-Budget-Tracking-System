from django.urls import path
from .views  import Registeration,Login
from .usertoken import TokenVerfication
from .email_verification import EmailVerificationView
from .passwordauthview import ChangepasswordView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .passwordReset  import PasswordResetView, PasswordcomfirmReset,SetPasswordView,Logoutveiw
urlpatterns = [
   
    path('signup', Registeration.as_view(), name='singup'),
    path('login', Login.as_view(), name='login'),
     path('logout/', Logoutveiw.as_view(), name="logout" ),
    path('usertoken', TokenVerfication.as_view(), name="token" ),
    path('emailverify', EmailVerificationView.as_view(), name="otp" ),
    path('changepassword/', ChangepasswordView.as_view(), name="passwordate" ),
    path('reset-password/', PasswordResetView.as_view(), name="password-reset" ),
    path('reset-password-comfirm/<token>/<uidb64>/', PasswordcomfirmReset.as_view(), name="reset-password-comfirm" ),
    path('setuser-password/', SetPasswordView.as_view(), name="set-passsword" ),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   
]