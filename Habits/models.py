from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    test = models.CharField(max_length=2, blank=True, null=True)
    tagname = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100)

class Habit(models.Model):
    name = models.CharField(max_length=100)
    goal = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username