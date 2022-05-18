from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
    

class Habit(models.Model):
    name = models.CharField(max_length=100)
    goal = models.IntegerField(blank=False)
    task = models.CharField(max_length=20, blank=True)
    units = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.name