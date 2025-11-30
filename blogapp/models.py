from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blogmodel(models.Model):
    
    Title = models.CharField(max_length=100)
    Body = models.TextField()
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    
    