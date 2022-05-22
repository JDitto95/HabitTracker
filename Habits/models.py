from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
from datetime import datetime
# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
    

class Habit(models.Model):
    task = models.CharField(max_length=20, blank=True)
    goal = models.IntegerField(blank=False)
    units = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.task
    
    
class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name='record')
    amount = models.IntegerField()
    date = models.DateField(null=True, blank=True, default=datetime.now)
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['habit', 'date'], name='once_per_day')
            ]

    # def __str__(self):
    #     return self.amount