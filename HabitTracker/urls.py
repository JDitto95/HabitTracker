"""HabitTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Habits import views as habits_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    # path("accounts/logout/",views.log_out, name ='log_out'),
    path('',habits_views.list_habits, name='list_habits'),
    path('habits/<int:pk>/edit/', habits_views.edit_habit, name='edit_habit'),
    path('habits/add/', habits_views.add_habits, name='add_habits'),
    path('habits/<int:pk>/delete/', habits_views.delete_habit, name='delete_habit'),
    path('habits/<int:pk>/edit/', habits_views.edit_habit, name='edit_habit'),
    path('habits/<int:pk>/detail/', habits_views.habit_detail, name='habit_detail'),
    path('habit/<int:pk>/add_record/', habits_views.add_record, name='add_record'),
    path('habit/<int:pk>/record_detail/', habits_views.record_detail, name='record_detail'),
    path('habit/record/<int:pk>/edit_record/', habits_views.edit_record, name='edit_record')
]
