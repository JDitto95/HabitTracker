from django.shortcuts import get_object_or_404, render; 

from .models import Habit
# Create your views here.
def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habits/list_habits.html", {"habits": habits})