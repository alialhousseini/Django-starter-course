from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('programs/<int:id>', views.program_details, name='program_details'),
    path('programs/bachelor', views.bachelor_progs, name='bachelor_progs'),
    path('programs/master', views.master_progs, name='master_progs'),
]
