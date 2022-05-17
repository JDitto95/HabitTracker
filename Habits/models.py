from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    test = models.CharField(max_length=2, blank=True, null=True)
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username