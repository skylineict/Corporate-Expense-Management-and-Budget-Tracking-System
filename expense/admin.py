from django.contrib import admin
from .models import Category, Expenses


# Register your models here.dmin



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','image')



@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'category', 'description']

    


