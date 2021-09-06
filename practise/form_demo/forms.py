from django import forms
import django
from django.db.models.base import Model
from django.forms import fields, widgets
from django.forms.fields import BooleanField, CharField

from django.forms import ModelForm
from .models import Customer

# https://docs.djangoproject.com/en/3.2/topics/forms/

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)
    your_age = forms.IntegerField(label='Your age')
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    booleanField = forms.BooleanField(required=False)

class CustomerForm(ModelForm):
    # Extra Validator if any
    password= CharField(min_length=8,required=False)

    class Meta:
        model = Customer
        fields = '__all__' 
        labels = {'first_name':'Enter yout first name','last_name':'Enter yout last name'}
        error_messages ={'first_name':{'required':'Name required'},
                        'last_name':{'required':'Last name required'},
                        'password':{'required':'Password is required'}
                        } 
        widgets={'first_name':forms.TextInput,
                'last_name':forms.TextInput(attrs={'id':'ls_name','class':'myclass',
                'placeholder':'Write your last name here',}),
                'password':forms.PasswordInput()
                }                                                                                                                




                