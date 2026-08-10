from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return HttpResponse("Welcome to TaskFlow! {user}".format(user=request.user.username))

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

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
    )


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
    task = Task.objects.get(id = task_id, user = request.user)
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
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
    )