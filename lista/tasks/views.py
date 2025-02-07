from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskFrom, EditTaskFrom
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def taskList(request):
    
    search = request.GET.get('search')
    status = request.GET.get('status', None)

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif status:
        tasks = Task.objects.all().order_by('-id').filter(status=status,user=request.user)

    else:
       tasks_list = Task.objects.all().order_by('-id').filter(user=request.user)

       paginator = Paginator(tasks_list, 10)

       page = request.GET.get('page')

       tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks':tasks})



@login_required
def taskView(request,id):
    task = get_object_or_404(Task, pk=id)    
    return render(request, 'tasks/task.html', {'task':task})


@login_required
def newTask(request):

    if request.method == 'POST':
        form = TaskFrom(request.POST)
        
        
        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'pendente'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskFrom()
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required
def editTask(request,id):
    task = get_object_or_404(Task, pk=id) 
    form = EditTaskFrom(instance=task)

    if (request.method == 'POST'):
        form =EditTaskFrom(request.POST, instance=task)
        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html',{'form':form,'task':task})
    else:
        return render(request, 'tasks/edittask.html',{'form':form,'task':task})


@login_required
def deleteTask(request,id):
    task = get_object_or_404(Task, pk=id) 
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso')

    return redirect('/')

