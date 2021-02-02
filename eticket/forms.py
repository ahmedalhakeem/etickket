from django import forms
from django.forms import ModelForm
from eticket.models import User, Department, Section, Problems, ProblemType

class LoginForm(forms.Form):
    username = forms.CharField(label="",  required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password',}))


class Register_empForm(forms.Form):
    first_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name',}))
    last_name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name", }))
    email = forms.EmailField(label="", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter your email id', }))
    username = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your username',}))
    password = forms.CharField(label="", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your password', }))
    pc_code = forms.CharField(label="", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'PC-code', }))
    department = forms.ModelChoiceField(label="", required=False, queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Select Department',})) 
    section = forms.ModelChoiceField(label="", required=True, queryset=Section.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Select Section',})) 
    

class Tech_issuesForm(forms.Form):
    p_type = forms.ModelChoiceField(label="المشكلة", required=True,queryset=ProblemType.objects.all(), widget=forms.Select(attrs={'class': 'form-control',}))
    user = forms.ModelChoiceField(label="اسم المستخدم", required=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class':'form-control', }))



