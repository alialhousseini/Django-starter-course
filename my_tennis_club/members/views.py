from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Member

def home(request):
    return render(request, 'pages/home.html')

def all_members(request):
    members = Member.objects.all()
    data = {
        'members': members,
    }
    return render(request, 'pages/members.html', data)

def member_details(request, id):
    member = get_object_or_404(Member, pk=id)
    # member = Member.objects.get(id=id)
    data = {
        'member': member,
    }
    return render(request, 'pages/member_details.html', data)