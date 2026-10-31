from .models import task
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'login.html')


# Logout
def user_logout(request):
    logout(request)
    return redirect('login')


# Home
@login_required(login_url='login')
def home(request):
    tasks = task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = task.objects.filter(is_completed=True)

    return render(request, 'home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })


@login_required(login_url='login')
def addTask(request):
    if request.method == 'POST':
        task.objects.create(
            task=request.POST.get('task')
        )
    return redirect('home')


@login_required(login_url='login')
def mark_as_done(request, pk):
    completed = get_object_or_404(task, pk=pk)
    completed.is_completed = True
    completed.save()
    return redirect('home')


@login_required(login_url='login')
def delete(request, pk):
    completed = get_object_or_404(task, pk=pk)
    completed.delete()
    return redirect('home')


@login_required(login_url='login')
def mark_as_undone(request, pk):
    completed = get_object_or_404(task, pk=pk)
    completed.is_completed = False
    completed.save()
    return redirect('home')


@login_required(login_url='login')
def edit(request, pk):
    s = get_object_or_404(task, pk=pk)

    if request.method == 'POST':
        s.task = request.POST.get('task')
        s.save()
        return redirect('home')

    return render(request, 'edit.html', {'s': s})

