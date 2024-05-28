from django.contrib import admin
from  .models import Book

# Register your models here.

  
@admin.register(Book)
class booadmin(admin.ModelAdmin):
    list_display = ['title','sub_title','auther','is_bn' ]
