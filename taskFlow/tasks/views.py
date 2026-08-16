from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'tasks/register.html')

def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        messages.error(request, "Invalid username or password.")

    return render(request, 'tasks/login.html')

def user_logout(request):

    logout(request)

    return redirect('login')
# Old view before stage 9: Task Filtering 
# @login_required
# def task_list(request):
#     tasks = Task.objects.filter(user=request.user)

#     return render(
#         request,
#         'tasks/task_list.html',
#         {'tasks': tasks}
#     )

# New view of task_list at stage 9:
@login_required
def task_list(request):
    tasks = Task.objects.filter(user = request.user)

    # Dashboard statistics
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed = True).count()
    pending_tasks = tasks.filter(completed = False).count()
    high_priority_tasks = tasks.filter(priority = 'high').count()

    if total_tasks > 0:
        completion_percentage = (
            completed_tasks / total_tasks
        ) * 100
    else:
        completion_percentage = 0

    # Filtering tasks based on query parameters
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    search = request.GET.get('search')

    if status == 'pending':
        tasks = tasks.filter(completed = False)
    elif status == 'completed':
        tasks = tasks.filter(completed = True)

    if priority in ['low', 'medium', 'high']:
        tasks = tasks.filter(priority = priority)
    # Search functionality
    if search:
        tasks = tasks.filter(
            title__icontains = search
        ) | tasks.filter(
            description__icontains = search
        )

    # Rendering the task list template with context
    return render(request, 'tasks/task_list.html', {
        'tasks' : tasks,
        'current_status' : status,
        'current_priority' : priority,
        'search' : search,
        
        'total_tasks' : total_tasks,
        'completed_tasks' : completed_tasks,
        'pending_tasks' : pending_tasks,
        'high_priority_tasks' : high_priority_tasks,
        'completion_percentage': completion_percentage,
    })

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        due_date = request.POST['due_date']

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date if due_date else None
        )

        return redirect('task_list')

    return render(
        request,
        'tasks/task_form.html'
    )

@login_required
def edit_task(request, task_id):

    task = get_object_or_404(
        Task,
        id = task_id,
        user = request.user
    )
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.priority = request.POST['priority']
        due_date = request.POST['due_date']
        task.due_date = due_date if due_date else None
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(
        Task,
        id = task_id,
        user = request.user
    )
    if task.user != request.user :
        return render(request, '403.html', {
            'massage' : 'You are not allowed to delete this task'
        })
    elif request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Keep in mind always redirect to view
    return render(request, 'tasks/confirm_delete.html', {'task' : task})


@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(
        Task,
        id = task_id,
        user = request.user
    )
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('task_list')
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
    )