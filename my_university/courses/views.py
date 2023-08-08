from django.shortcuts import render
from .models import Course
# Create your views here.
def all_courses(request):
    courses = Course.objects.all()
    data = {
        'courses':courses,
    }
    return render(request, 'pages/all_courses.html', data)