from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
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
    
    
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='Record')
    amount = models.IntegerField()
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['habit', 'created_at'], name='Habit')
            ]

    def __str__(self):
        return self.amount