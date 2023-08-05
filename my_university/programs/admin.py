from django.contrib import admin
from .models import Program

class ProgramAdmin(admin.ModelAdmin):
    list_display= ('title', 'program_type')
    
    
admin.site.register(Program, ProgramAdmin)