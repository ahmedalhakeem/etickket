from django import forms
from django.forms import ModelForm
from eticket.models import User, Department, Section, Problems, ProblemType

class LoginForm(forms.Form):
    username = forms.CharField(label="",  required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))