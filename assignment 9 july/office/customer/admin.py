  
from django.contrib import admin

# Register your models here.
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age','email', 'contact_no','photo')
    list_filter = ('id',) 


admin.site.register(Customer, CustomerAdmin)