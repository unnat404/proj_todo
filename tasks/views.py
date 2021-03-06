from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.
def index(request):
    # return HttpResponse("Hello World!")

    tasks=Task.objects.all()

    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context={'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',context)

def updateTask(request,pk):
    task=Task.objects.get(id=pk)

    form = TaskForm(instance=task) # this creastes a form of object type task and prefills everything in the above form manner
    if request.method =='POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form}
    return render(request,'tasks/update_task.html',context)

def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    context={'item':item}
    if request.method =='POST':
        form = TaskForm(request.POST,instance=item)
        item.delete()
        return redirect("/")

    return render(request,'tasks/delete.html',context)
