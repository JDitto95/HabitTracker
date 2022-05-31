from django.urls import path
from api import views as api_views


urlpatterns = [
    path('', api_views.api_root),
    path('habits/', api_views.HabitListView.as_view(), name="api-habit-list"),
    path('habits/create/', api_views.HabitCreateView.as_view(), name="api-habit-create"),
    path('habits/<int:pk>/', api_views.HabitDetailView.as_view(), name='habit-detail-api'),
    # path('habits/<int:pk>/delete/', api_views.HabitDeleteView.as_view(), name='api-delete')
]