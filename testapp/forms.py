from django import forms   
from django.contrib.auth.models import User   
from testapp.models import Event_model

from typing import Any
class SignUpForm(forms.ModelForm): 
    class Meta: 
                 
        model=User
        fields=['username','password','email','first_name','last_name',] 
        help_texts = {
            'username': None,  # This removes the help text
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter your email address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter your password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter your last name'}),
        }
    
class create_event_form(forms.ModelForm):
    class Meta:
        model = Event_model
        fields="__all__"
        widgets = {
            'eventname': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter event name'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter date (mm/dd/yyyy)'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Enter event location'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'type_of_event': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;', 'placeholder': 'Specify type of event'}),
        }
