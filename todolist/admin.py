from django.contrib import admin
from .models import Todolist

# Register your models here.
# Create your models here.
@admin.register(Todolist)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('name','description','is_complete', 'create_by')
   