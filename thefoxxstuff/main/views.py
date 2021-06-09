from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def tasks(request):
    tasks = Task.objects.order_by('-id')[:5]
    return render(request, 'main/tasks.html', {'tasks':tasks})


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Форма говно'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
    