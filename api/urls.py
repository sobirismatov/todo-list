from django.urls import path
from .views import (
    get_task,
    mark_task,
    get_completed_tasks,
    get_incompleted_tasks,
    create_task,
    update_task,
    delete_task,
    Get_all,
)

urlpatterns = [
    path('tasks', Get_all.as_view()),
    path('tasks/<int:id>', get_task),
    path('tasks/<int:id>/complete', mark_task),
    path('tasks/completed', get_completed_tasks),
    path('tasks/incompleted', get_incompleted_tasks),
    path('tasks/incompleted', get_incompleted_tasks),
]