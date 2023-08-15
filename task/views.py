from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form' : form}
    return render(request, 'task/index.html', context)


def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'task/task_update.html', context)