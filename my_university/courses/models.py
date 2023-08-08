from django.db import models
from programs.models import Program

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField()
    programs = models.ManyToManyField(Program, related_name='programs')
    