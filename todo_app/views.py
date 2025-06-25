from django.shortcuts import render
from todo.models import Task

def index(request):
  task = Task.objects.filter(is_completed=False).order_by('-updated_at')
  completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
  context = {
      'tasks': task,
      'completed_tasks': completed_tasks,
  }
  return render(request, 'index.html', context)