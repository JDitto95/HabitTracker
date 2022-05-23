
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit, Record
from .forms import HabitForm, RecordForm
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

    return render( request, "habits/edit_habit.html", {"form": form, "habit": habit})

@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='list_habits')
    return render(request, "habits/delete_habit.html", {"habit": habit}) 


    
def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    records = Record.objects.filter(habit=habit.pk)
    return render(request, "habits/habit_detail.html", {"habit": habit, "records": records })  

def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'GET':
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.habit = habit
            new_record.save()
            return redirect('habit_detail', pk=pk)

    return render(request, "habits/add_record.html", {"form": form, "habit": habit})  



def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, "habits/record_detail.html", { "record": record })


def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(data=request.POST, instance=record)
        if form.is_valid():
            record=form.save(commit=False)
            form.save()
            return redirect(to='record_detail', pk=pk)

    else:
        form = RecordForm( instance=record)
        
    return render( request, "habits/edit_record.html", {"form": form, "record": record})           
# def log_out(request):
#     logout(request)
#     return redirect('log_out')


