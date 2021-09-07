from django import forms
from django.forms import fields
from .models import Book

class FileUploadForm(forms.Form):
    title = forms.CharField(max_length=100,required=True)
    file = forms.FileField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        