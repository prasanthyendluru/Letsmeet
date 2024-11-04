from django import forms   
from django.contrib.auth.models import User   
from testapp.models import Event_model

class SignUpForm(forms.ModelForm):   
    class Meta:          
        model=User
        fields=['username','password','email','first_name','last_name']  
        help_texts = {
            'username': None,  # This removes the help text
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),

        }
class create_event_form(forms.ModelForm):
    class Meta:
        model = Event_model
        fields="__all__"
        widgets = {
            'eventname': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),
            'type_of_event': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 30%;'}),

        }