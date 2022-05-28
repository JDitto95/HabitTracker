from django.urls import path, include
from api import views as api_views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'habit', api_views.HabitModelViewSet)

urlpatterns = [
    path('habits/', api_views.HabitListView.as_view(), name="api-habit-list"),
    path('api/habits/create/', api_views.HabitCreateView.as_view(), name="api-habit-create"),
    # path('', include(router.urls)),
    path('habit/<int:pk>/', api_views.HabitDetailView.as_view(), name="habit-detail-api"),
    path('api/habit/<int:pk>/delete/', api_views.HabitDelete.as_view(),name="api-habit-delete"),
    
]