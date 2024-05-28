from  authencation.models import User
from django.db import models
from expense.models import Category



class Income(models.Model):
    name = models.CharField( max_length=500)
    amount = models.DecimalField( max_digits=10, decimal_places=2)
    source = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='income')
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date']