from django.contrib import admin
from .models import Person,Technology
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'email')
    list_filter = ('is_verify',) 

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'technology')
    list_filter = ('technology',) 

admin.site.register(Person, PersonAdmin)
admin.site.register(Technology, TechnologyAdmin)
