from django import forms

from .models import Habit, User, Record

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'description',
            'task',
            'goal',
            'units',
        ]

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'amount',
        ]
    