from django.contrib import admin
from .models import *

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school_id')
    list_filter = ('school_id',) 

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no')
    list_filter = ('roll_no',)


admin.site.register(School,SchoolAdmin)
admin.site.register(Student,StudentAdmin)
