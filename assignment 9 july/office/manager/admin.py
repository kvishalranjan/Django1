from django.contrib import admin
from .models import Manager, Room

# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age','email', 'contact_no','photo')
    list_filter = ('id',) 
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'room_type', 'price', 'capacity','contact_no')
    list_filter = ('room_type',) 


admin.site.register(Manager, ManagerAdmin)
admin.site.register(Room, RoomAdmin)