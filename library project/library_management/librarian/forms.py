from django import forms
from django.contrib.auth.models import User
from . import models
from .models import IssuedBook, Librarian




class LibrarianSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['bookname','isbn','authorname','category']


class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


class IssuedBookForm(forms.ModelForm):
    class Meta:
        model=IssuedBook
        fields="__all__"
    

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']


