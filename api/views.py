from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import Habits
from api.serializers import HabitSerializer
from Habits.models import Habit
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework import reverse, generics
# Create your views here.

# @api_view([GET])
def api_root(request, format=None):
    return Response({
        'habits': reverse('habit-list-api', request=request, format=format)
    })
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



# class HabitDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Habit.objects.filter()
    # serializer_class = HabitSerializer
    
    # def delete(self,request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    
    
    
class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer 
    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
    def porform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def porform_update(self, serializer):
        serializer.save(user=self.request.user)