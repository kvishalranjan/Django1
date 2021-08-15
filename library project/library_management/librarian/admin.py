from django.contrib import admin
from .models import Book, IssuedBook, Librarian
from .models import Student

# Register your models here.
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'DOB','email', 'contactno','photo')
    list_filter = ('id',) 

class BookAdmin(admin.ModelAdmin):
    list_display = ('bookname','authorname','isbn','category')
    list_filter = ('category',)

class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('enrollment','isbn','issuedate','expirydate')
    list_filter = ('issuedate',)

admin.site.register(Librarian,LibrarianAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(IssuedBook,IssuedBookAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'DOB','email', 'contactno','photo')
    list_filter = ('id',) 


admin.site.register(Student, StudentAdmin)