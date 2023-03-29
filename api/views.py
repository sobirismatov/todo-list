from django.http import HttpRequest, JsonResponse
from .models import Task

def get_all(request: HttpRequest) -> JsonResponse:
    '''get all tasks'''
    tasks = Task.objects.all()
    data = {'tasks': []}

    for task in tasks:
        data['tasks'].append({
            'id': task.id,
            'name': task.name,
            'completed': task.completed,
            'desciption': task.description,
            'created': task.created,
            'updated': task.updated,
        })

    return JsonResponse(data)