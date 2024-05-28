from  authencation.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category")
    description = models.TextField()


    def __str__(self):
        return self.name


class Expenses(models.Model):
    name = models.CharField( max_length=500)
    amount = models.DecimalField( max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='source')
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name