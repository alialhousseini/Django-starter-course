from django.db import models

# Create your models here.
class Program(models.Model):
    
    choices_type =(
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    program_type = models.CharField(choices=choices_type)
    
    