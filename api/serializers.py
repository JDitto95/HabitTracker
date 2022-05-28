from rest_framework import serializers
from Habits.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id',
            'task',
            'goal',
            'units',
            'user_id',
        )
        