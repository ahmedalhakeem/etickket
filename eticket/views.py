from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from .forms import *
from django.db import IntegrityError
from django.urls import reverse
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
            print(login_user.group)
            if login_user.groups == "office manager":
                login(request, login_user)
    
            else:
                return render(request, "eticket/login_manager.html",{
                    "message": "You have no privilge access"
                })
            return render (request, 'eticket/manager_profile.html')
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



def register_emp(request):
    # if method is post!
    if request.method == "POST":
        new_user = Register_empForm(request.POST or None)
        if new_user.is_valid():
            first_name = new_user.cleaned_data['first_name']
            last_name = new_user.cleaned_data['last_name']
            email = new_user.cleaned_data['email']
            username = new_user.cleaned_data['username']
            password = new_user.cleaned_data['password']
            pc_code = new_user.cleaned_data['pc_code']
            department = new_user.cleaned_data['department']
            section = new_user.cleaned_data['section']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, 
            username=username, password=password,pc_code=pc_code, department=department, section=section)
            user.save()
            return HttpResponseRedirect(reverse('profile_emp', args=(user.id,)))
    else:
        new_user=Register_empForm()
        return render(request, 'eticket/register_emp.html',{
            "user": new_user
        })
# Profile page for each employee   
def profile_emp(request, emp_id):
    user = User.objects.get(pk=emp_id)
    if user is not None:
        return render(request, "eticket/profile_emp.html",{
            "user": user            
        })
def manager_profile(request):
    return render(request, "eticket/manager_profile.html")