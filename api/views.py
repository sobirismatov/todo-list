from django.http import HttpRequest, JsonResponse
from .models import Task
import json
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.contrib.auth import authenticate
from base64 import b64decode
from django.contrib.auth.models import User

def to_dict(task):
    data = {
        'id': task.id,
        'name': task.name,
        'completed': task.completed,
        'desciption': task.description,
        'created': task.created,
        'updated': task.updated,
        'user': task.user.username
    }
    return data

class Tasks(View):
    def get(self, request: HttpRequest, id=None) -> JsonResponse:
        '''get all tasks'''
        authorization = request.headers.get('Authorization').split()[1]
        
        username, password = b64decode(authorization).decode().split(':')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if id == None:
                tasks = Task.objects.filter(user=user)
                data = {'tasks': []}

                for task in tasks:
                    data['tasks'].append(to_dict(task))

                return JsonResponse(data)
            else:
                try:
                    task = Task.objects.get(id=id)
                    return JsonResponse(to_dict(task))
                except ObjectDoesNotExist:
                    return JsonResponse({"status": "does not exist"})
        
        return JsonResponse({'status': 'Unauthorized'})
    def post(self, request: HttpRequest) -> JsonResponse:
        """
        Creta todo task
        """
        if request.method == 'POST':
            body = request.body
            # decode body
            decode = body.decode()
            data = json.loads(decode)
            name = data.get('name')
            completed = data.get('completed')
            description = data.get('description')

            if name == None:
                return JsonResponse({"status": "name field is required."})
            if description == None:
                return JsonResponse({"status": "description field is required."})
            
            task = Task.objects.create(
                name = name,
                completed = completed,
                description = description
            )
            task.save()
            return JsonResponse({"status": "Saccessfuly!"})
        else:
            return JsonResponse({"status": "You need POST request!"})
    
class Delete(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        """
        delete task
        """
        if request.method == "GET":
            try:
                # get product from database by id
                product = Task.objects.get(id=pk)
                product.delete()
                return JsonResponse(to_dict(product))
            except ObjectDoesNotExist:
                return JsonResponse({"status": "object doesn't exist"})
   
class Update(View):
    def post(self, request: HttpRequest, pk: int) -> JsonResponse:
        if request.method == "POST":
            try:
                task = Task.objects.get(id=pk)
            except:
                return JsonResponse({"status": "Does not exist!"})
            
            body = request.body
            # decode body
            decode = body.decode()
            data = json.loads(decode)
            name = data.get('name')
            completed = data.get('completed')
            description = data.get('description')

            task.name = data['name']
            task.description = data['description']
            task.completed = data['completed']
            task.save()
            return JsonResponse({"status": "Saccessfuly updated!"})

class CompletedTasks(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        tasks = Task.objects.filter(completed=True)
        data = {
            'tasks': []
        }
        for task in tasks:
            data['tasks'].append(to_dict(task))

        return JsonResponse(data)
    
class InCompletedTasks(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        tasks = Task.objects.filter(completed=False)
        data = {
            'tasks': []
        }
        for task in tasks:
            data['tasks'].append(to_dict(task))

        return JsonResponse(data)