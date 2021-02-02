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
    
def login_master(request):
    # if post method!
    if request.method == "POST":
        loginform = LoginForm(request.POST or None)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            
            
            login_user = authenticate(request, username=username, password=password)

            if login_user.groups.filter(name="office manager").exists():

                login(request, login_user)
                return HttpResponseRedirect(reverse('manager_profile',args=(login_user.id,)))
                
    
            elif login_user.groups.filter(name="dept manager").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('dept_mgr_profile',args=(login_user.id,)))
                #return render(request, 'eticket/dep_mgr_profile.html')

            elif login_user.groups.filter(name="section mgr").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('sec_mgr_profile',args=(login_user.id,)))
                #return render(request, "eticket/sec_mgr_profile.html")

            elif login_user.groups.filter(name="technical team").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('it_profile',args=(login_user.id,)))
                #return render(request, "eticket/it_profile.html")

            elif login_user.groups.filter(name="employees").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('profile_emp',args=(login_user.id,)))
                #return render(request, "eticket/profile_emp.html")
            
            else: 
                return render(request, "eticket/error.html",{
                    "message": "You have no privilge access"
                })
    # if get method!
    else:
        loginform= LoginForm()
        return render(request, 'eticket/login_master.html',{
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
            
            if user.section =! "IT":
                user.groups.add(5)
            else:
                user.groups.add(4)
            return HttpResponseRedirect(reverse('login_master'))
            user.save()
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
# profile page for manager
def manager_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "eticket/manager_profile.html",{
        "user": user
    })
# profile page for it team
def it_profile(request, user_id):
    it_user = User.objects.get(pk=user_id)
    return render (request, "eticket/it_profile.html",{
        "user": it_user
    })
# profile page for department manager
def dept_mgr_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "eticket/dept_mgr_profile.html",{
        "user": user
    })
# profile page for section manager
def sec_mgr_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'eticket/sec_mgr_profile.html',{
        "user": user
    })