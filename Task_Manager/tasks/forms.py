# Importing necessary modules
from django import forms  # Used to create forms
from .models import Task  # Importing the Task model from the current app
from django.contrib.auth.models import User  # Importing the User model for user-related forms
from django.contrib.auth.forms import UserCreationForm  # Used for creating user signup forms
from datetime import date  # For comparing dates (used in validation)

# TaskForm - Form to create or update tasks
class TaskForm(forms.ModelForm): 
    # Meta class defines the model and fields to be used in the form
    class Meta: 
        model = Task  # The form is based on the Task model
        fields = ['title', 'description', 'status', 'due_date']  # Fields to include in the form
        widgets = { 
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Customizing widget for title (input box)
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),  # Customizing widget for description (textarea with rows=4)
            'status': forms.Select(attrs={'class': 'form-select'}),  # Customizing widget for status (dropdown select)
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Customizing widget for due date (date picker)
        } 

    # Custom validation for the due date field
    def clean_due_date(self): 
        # Get the cleaned data for due_date from the form
        due_date = self.cleaned_data.get('due_date')  
        
        # Check if the due date is in the past
        if due_date and due_date < date.today():  
            # Raise an error if the due date is in the past
            raise forms.ValidationError("Due date cannot be in the past.")  
        
        # Return the due date if validation passes
        return due_date 

# SignupForm - Form to create a new user account
class SignupForm(UserCreationForm):  
    # Defining additional fields for the user signup form
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  # Email input field with class 'form-control'
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # Username input field with class 'form-control'
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # Password field with class 'form-control'
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # Confirm password field with class 'form-control'

    # Meta class defines the model and fields to be used for the signup form
    class Meta: 
        model = User  # The form is based on the User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields to include in the form