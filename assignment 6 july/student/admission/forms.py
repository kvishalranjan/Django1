from django import forms
from .models import Student_admission

class Student_admissionForm(forms.ModelForm):
    class Meta:
        model = Student_admission
        fields = "__all__"