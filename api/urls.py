from django.urls import path
from .views import get_all


urlpatterns = [
    path('tasks', get_all)
]