from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('members/', views.all_members, name='all_members'),
    path('members/details/<int:id>', views.member_details, name='member_details'),
]
