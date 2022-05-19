
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm
# Create your views here.
@login_required
def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habits/list_habits.html", {"habits": habits})
@login_required
def add_habits(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            Habit = form.save(commit=False)
            Habit.user = request.user
            Habit.save()
            return redirect(to='list_habits')
            
    return render( request, "habits/add_habit.html", {"form": form})
@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')
    return render(request, "habits/delete_habit.html", {"habit": habit}) 

@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='list_habits')

    return render(request, "habits/edit_habit.html", {
        "form": form,
        "habit": habit
    })     
    
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    # notes = Note.objects.filter(contact_id=contact.pk)
    
    return render(request, "habits/habit_detail.html", {"habit": habit })  

# def log_out(request):
#     logout(request)
#     return redirect('log_out')
