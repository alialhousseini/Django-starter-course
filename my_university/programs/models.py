from django.db import models

# Create your models here.
class Program(models.Model):
    
    choices_type =(
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    program_type = models.CharField(max_length=200, choices=choices_type)
    
    def __str__(self):
        return f"{self.title}"