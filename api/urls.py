from django.urls import path
from api import views as api_views


urlpatterns = [
    path('habits/', api_views.HabitListView.as_view(), name="api-habit-list"),
    # path('habits/api/create/', api_views.HabitCreateView.as_view(), name="api-habit-create"),
    path('habit/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit-detail-api'),
]