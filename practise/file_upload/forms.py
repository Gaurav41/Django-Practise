from django import forms

class FileUploadForm(forms.Form):
    title = forms.CharField(max_length=100,required=True)
    file = forms.FileField()
