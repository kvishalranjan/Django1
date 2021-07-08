from django.contrib import admin
from .models import PredResults
# Register your models here.

class IrisAdmin(admin.ModelAdmin):
    list_display = ('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Id')
    list_filter = ('Id',) 


admin.site.register(PredResults, IrisAdmin)