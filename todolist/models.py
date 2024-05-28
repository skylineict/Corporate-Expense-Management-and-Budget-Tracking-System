from django.db import models
from django.contrib.auth import get_user_model
from helperclass.models import Modeltracking

User = get_user_model()

# Create your models here.
class Todolist(Modeltracking):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

