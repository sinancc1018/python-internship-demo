# Importing necessary modules
from django.shortcuts import render, redirect, get_object_or_404  # Used for rendering templates, redirecting, and fetching objects
from .models import Task  # Importing the Task model
from .forms import TaskForm, SignupForm  # Importing the forms for tasks and signup
from django.contrib.auth.decorators import login_required  # Ensures only logged-in users can access the views
from django.contrib.auth import login  # Used to log the user in

# View to handle user signup
def signup_view(request): 
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = SignupForm(request.POST)  # Create a form with the submitted data
        if form.is_valid():  # Check if the form is valid
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in immediately after registration
            return redirect('dashboard')  # Redirect to the dashboard after successful signup
    else:  # If the request method is GET, show an empty signup form
        form = SignupForm()  
    return render(request, 'tasks/signup.html', {'form': form})  # Render the signup page with the form

# View to show the user’s dashboard, with task statistics
@login_required 
def dashboard(request): 
    tasks = Task.objects.filter(created_by=request.user)  # Fetch all tasks created by the logged-in user
    total_tasks = tasks.count()  # Count total tasks
    completed_tasks = tasks.filter(status='Completed').count()  # Count completed tasks
    pending_tasks = tasks.filter(status='Pending').count()  # Count pending tasks
    
    context = {  # Prepare the context to send data to the template
        'total_tasks': total_tasks, 
        'completed_tasks': completed_tasks, 
        'pending_tasks': pending_tasks, 
    } 
    return render(request, 'tasks/dashboard.html', context)  # Render the dashboard page with task statistics

# View to show all tasks created by the logged-in user
@login_required 
def task_list(request): 
    tasks = Task.objects.filter(created_by=request.user).order_by('-id')  # Fetch tasks ordered by the most recent
    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Render the task list page with the tasks

# View to show the details of a specific task
@login_required 
def task_detail(request, id): 
    task = get_object_or_404(Task, id=id, created_by=request.user)  # Get task by ID, ensuring it belongs to the logged-in user
    return render(request, 'tasks/task_detail.html', {'task': task})  # Render the task detail page with the task data

# View to create a new task
@login_required 
def task_create(request): 
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = TaskForm(request.POST)  # Create a form with the submitted data
        if form.is_valid():  # Check if the form is valid
            task = form.save(commit=False)  # Save the form but don’t commit to the database yet
            task.created_by = request.user  # Assign the logged-in user as the creator of the task
            task.save()  # Save the task to the database
            return redirect('task_list')  # Redirect to the task list after creation
    else:  # If the request method is GET, show an empty task creation form
        form = TaskForm()  
    return render(request, 'tasks/task_form.html', {'form': form, 'page_title': 'Create Task'})  # Render the task creation form

# View to update an existing task
@login_required 
def task_update(request, id): 
    task = get_object_or_404(Task, id=id, created_by=request.user)  # Get the task by ID and ensure it belongs to the logged-in user
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = TaskForm(request.POST, instance=task)  # Bind the form with the existing task data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the updated task
            return redirect('task_list')  # Redirect to the task list after updating
    else:  # If the request method is GET, pre-fill the form with the task data for editing
        form = TaskForm(instance=task)  
    return render(request, 'tasks/task_form.html', {'form': form, 'page_title': 'Update Task'})  # Render the task update form

# View to delete a task
@login_required 
def task_delete(request, id): 
    task = get_object_or_404(Task, id=id, created_by=request.user)  # Get the task by ID and ensure it belongs to the logged-in user
    if request.method == 'POST':  # If the form is submitted (POST request)
        task.delete()  # Delete the task from the database
        return redirect('task_list')  # Redirect to the task list after deletion
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})  # Render a confirmation page before deletion