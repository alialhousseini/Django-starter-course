from django.shortcuts import render, get_object_or_404
from .models import Program

# Create your views here.
def home(request):
    programs = Program.objects.all()
    data= {
        'programs':programs
    }
    return render(request, 'pages/home.html', data)

def program_details(request, id):
    program = get_object_or_404(Program, pk=id)
    data = {
        'program':program
    }
    return render(request, 'pages/program_details.html', data)

def bachelor_progs(request):
    programs = Program.objects.all().filter(program_type='Bachelor')
    data= {
        'programs':programs
    }
    return render(request, 'pages/bachelor_progs.html', data)

def master_progs(request):
    programs = Program.objects.all().filter(program_type='Master')
    data= {
        'programs':programs
    }
    return render(request, 'pages/master_progs.html', data)