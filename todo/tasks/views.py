from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):             ##index function takes an HTTPrequest object as its first parameter. Here parameter is request
    tasks = Task.objects.all()  ##All the objects

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()             ##Saving the form after a task is given
        return redirect('/')        ##To return to the TODOlist

    context = {'tasks' :tasks, 'form':form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):       ##Lets us update the task
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST' :
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')        

    context = {'form': form}
    
    return render(request, 'tasks/update_task.html', context)  ##render it to update_task.html

def deleteTask(request, pk):        ##Lets us delete the task
    item = Task.objects.get(id=pk)

    if request.method == 'POST' :
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)    ##render it to delete.html
