from django.shortcuts import get_object_or_404, render, redirect

from .models import Habit
from .forms import HabitForm
# Create your views here.
def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habits/list_habits.html", {"habits": habits})

def add_habits(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')
            
    return render( request, "habits/add_habit.html", {"form": form})

def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')