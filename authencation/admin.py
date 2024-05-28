from django.contrib import admin
from .models import User,UserVerification


# Register your models here.dmin



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','is_active',"email",'is_verifiedemail','otp_code','otp_sent_time')



@admin.register(UserVerification)
class UserVerifcationAdmin(admin.ModelAdmin):
    list_display = ('verification_code','user')


