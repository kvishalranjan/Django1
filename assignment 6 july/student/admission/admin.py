from django.contrib import admin

# Register your models here.
from .models import Student_admission
# Register your models here.

class Student_admissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'gender','dateofbirth', 'city','phone',"is_verify")
    list_filter = ('age',) 


admin.site.register(Student_admission, Student_admissionAdmin)
