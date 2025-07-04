from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from todo.models import Task

# Create your views here.
def addTask(request):
    task = request.POST.get('task')
    if task:
        new_task = Task(task=task)
        new_task.save()
    return redirect('index')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('index')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('index')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('index')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request, 'edit_task.html', context)
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')