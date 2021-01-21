from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,  
from .forms import *
# Create your views here.
def index(request):

    return render(request, 'eticket/index.html')
def login_manager(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            login_user = authenticate(request, username=username, password=password)
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_manager.html',{
            "loginform": loginform
        })

def login_dep_mgr(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            login_user = authenticate(request, username=username, password=password)
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_dep_mgr.html',{
            "loginform": loginform
        })

def login_sec_mgr(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            login_user = authenticate(request, username=username, password=password)
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_sec_mgr.html',{
            "loginform": loginform
        })

def login_it(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            login_user = authenticate(request, username=username, password=password)
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_it.html',{
            "loginform": loginform
        })
        
def login_emp(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            login_user = authenticate(request, username=username, password=password)
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_emp.html',{
            "loginform": loginform
        })

@login_required
def register_emp(request):
    return
