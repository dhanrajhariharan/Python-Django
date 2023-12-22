from django.shortcuts import render, redirect
from .models import Department, User, Task

def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department_id = request.POST.get('department')
        department = Department.objects.get(pk=department_id)
        User.objects.create(name=name, department=department)
        return redirect('create_user')

    departments = Department.objects.all()
    return render(request, 'create_user.html', {'departments': departments})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        department_id = request.POST.get('department')
        department = Department.objects.get(pk=department_id)
        Task.objects.create(title=title, description=description, department=department)
        return redirect('create_task')

    departments = Department.objects.all()
    return render(request, 'create_task.html', {'departments': departments})

def assign_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        user_id = request.POST.get('user')
        user = User.objects.get(pk=user_id)
        task.assigned_to = user
        task.save()
        return redirect('assign_task', task_id=task_id)

    users = User.objects.filter(department=task.department)
    return render(request, 'assign_task.html', {'task': task, 'users': users})


def task_report(request):
    tasks = Task.objects.all()
    return render(request, 'task_report.html', {'tasks': tasks})

