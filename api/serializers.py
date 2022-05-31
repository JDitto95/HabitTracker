from rest_framework import serializers
from Habits.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'pk',
            'task',
            'goal',
            'units',
        )
        