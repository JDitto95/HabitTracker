from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import HabitSerializer
from .models import Habit

# Create your views here.
class HabitListView(APIView):
    def get(self, request, format=None):
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)