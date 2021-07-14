from django.contrib import admin
from .models import *
# Register your models here.
class AadharAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name',) 

class PersonAdmin(admin.ModelAdmin):
    list_display = ('identity', 'name')
    list_filter = ('name',)

admin.site.register(Aadhar, AadharAdmin)
admin.site.register(Person, PersonAdmin)


