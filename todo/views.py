from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def addTask(request):
    task =request.POST['task']
    task.objects.create(task=task)
    return redirect('home')