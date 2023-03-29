from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Task


def to_dict(task: Task) -> dict:
    '''to dict'''
    return {
        'id': task.id,
        'name': task.name,
        'completed': task.completed,
        'desciption': task.description,
        'created': task.created,
        'updated': task.updated,
    }

def get_all(request: HttpRequest) -> JsonResponse:
    '''get all tasks'''
    tasks = Task.objects.all()
    data = {'tasks': []}

    for task in tasks:
        data['tasks'].append(to_dict(task))

    return JsonResponse(data)

def get_task(request: HttpRequest, id: int) -> JsonResponse:
    '''get task by id'''
    try:
        task = Task.objects.get(id=id)
        return JsonResponse(to_dict(task))
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

def create_task(request: HttpRequest) -> JsonResponse:
    '''create task'''
    data = request.body.decode('utf-8')
    data = json.loads(data)
    task = Task.objects.create(
        name=data['name'],
        description=data['description'],
        completed=data['completed']
    )
    return JsonResponse(to_dict(task))

def mark_task(request: HttpRequest, id: int) -> JsonResponse:
    '''mark task'''
    try:
        task = Task.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)
    
    task.completed = not task.completed
    task.save()

    return JsonResponse(to_dict(task))

def get_completed_tasks(request: HttpRequest) -> JsonResponse:
    '''get tasks by completed'''
    tasks = Task.objects.filter(completed=True)
    data = {'tasks': []}

    for task in tasks:
        data['tasks'].append(to_dict(task))

    return JsonResponse(data)

def get_incompleted_tasks(request: HttpRequest) -> JsonResponse:
    '''get tasks by completed'''
    tasks = Task.objects.filter(completed=False)
    data = {'tasks': []}

    for task in tasks:
        data['tasks'].append(to_dict(task))

    return JsonResponse(data)

def update_task(request: HttpRequest, id: int) -> JsonResponse:
    '''update task'''
    try:
        task = Task.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    data = request.body.decode('utf-8')
    data = json.loads(data)

    task.name = data['name']
    task.description = data['description']
    task.completed = data['completed']
    task.save()

    return JsonResponse(to_dict(task))

def delete_task(request: HttpRequest, id: int) -> JsonResponse:
    '''delete task'''
    try:
        task = Task.objects.get(id=id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    task.delete()
    return JsonResponse({'message': 'Task deleted'})
