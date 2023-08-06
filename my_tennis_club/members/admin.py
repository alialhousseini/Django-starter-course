from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name','phone')
    search_fields = ['last_name']
    list_filter = ('first_name', 'joined_date')
    
# Register your models here.
admin.site.register(Member, MemberAdmin)