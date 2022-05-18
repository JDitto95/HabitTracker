from django import forms



from .models import Habit, User

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'name',
            'goal',
            'task',
            'units',
            
        ]