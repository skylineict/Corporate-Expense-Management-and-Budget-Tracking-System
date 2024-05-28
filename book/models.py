from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    sub_title =models.CharField(max_length=200)
    auther = models.CharField(max_length=200)
    is_bn =  models.CharField(max_length=200)


    def __str__(self):
        return self.title
    