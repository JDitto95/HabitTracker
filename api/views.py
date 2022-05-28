from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import HabitSerializer
from Habits.models import Habit
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveDestroyAPIView
# Create your views here.
class HabitListView(APIView):
    def get(self, request, format=None):
        # breakpoint()
        habits = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
    
class HabitCreateView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
    
        serializer.save(user=self.request.user)
        
class HabitDelete(RetrieveDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
class HabitModelViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer 


class HabitDetailView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer 
