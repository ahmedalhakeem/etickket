from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from .forms import *
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.models import Group
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
            
            if login_user.groups.filter(name="office manager").exists():

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
            if login_user.groups.filter(name="dept manager").exists():
                login(request, login_user)
            else:
                return render(request, 'eticket/error.html',{
                    'message': 'you have no valid access'
                })
            return render(request, 'eticket/dep_mgr_profile.html')            

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
            if login_user.groups.filter(name = 'section mgr').exists():
                login(request, login_user)
            else:
                return render(request, 'eticket/login_sec_mgr.html',{
                    'message': "you have no valid access"
                })
            return render (request, 'eticket/sec_mgr_profile.html')
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
            # verify if the user belongs to it team
            if login_user.groups.filter(name='technical team').exists():
                login(request, login_user)
            else:
                return render(request, 'eticket/login_it.html',{
                    "message": "نعتذر , ليس لديك الصلاحية للدخول الى هذه الصفحة"
                })
            return HttpResponseRedirect(reverse('it_profile', args=(login_user.id,)))

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
def it_profile(request, user_id):
    it_user = User.objects.get(pk=user_id)
    return render (request, 'eticket/it_profile.html',{
        "user": it_user
    })