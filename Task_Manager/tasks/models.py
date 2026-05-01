from django.db import models 
from django.contrib.auth.models import User 
 
class Task(models.Model): 
    STATUS_CHOICES = [ 
        ('Pending', 'Pending'), 
        ('Completed', 'Completed'), 
    ] 
 
    title = models.CharField(max_length=200) 
    description = models.TextField() 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') 
    due_date = models.DateField(null=True, blank=True) 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 
 
    def __str__(self): 
        return self.title 