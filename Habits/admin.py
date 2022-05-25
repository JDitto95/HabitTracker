from django.contrib import admin
from .models import Habit, User, Record
# Register your models here.
admin.site.register(Habit)
admin.site.register(User)
admin.site.register(Record)