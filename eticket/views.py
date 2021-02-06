from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from .forms import *
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.models import Group
from .models import User, Section, Department, Tickets
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

            if login_user.groups.filter(name="manager").exists():

                login(request, login_user)
                return HttpResponseRedirect(reverse('manager_profile',args=(login_user.id,)))
                
    
            elif login_user.groups.filter(name="department_manager").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('dept_mgr_profile',args=(login_user.id,)))
                #return render(request, 'eticket/dep_mgr_profile.html')

            elif login_user.groups.filter(name="section manager").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('sec_mgr_profile',args=(login_user.id,)))
                #return render(request, "eticket/sec_mgr_profile.html")

            elif login_user.groups.filter(name="tech").exists():
                login(request, login_user)
                return HttpResponseRedirect(reverse('it_profile',args=(login_user.id,)))
                #return render(request, "eticket/it_profile.html")

            elif login_user.groups.filter(name="employee").exists():
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

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

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
            
            it_section = Section.objects.get(section_name="IT")
            print(it_section)
            if user.section != it_section:
                x=True
                user.groups.add(5)
            else:
                x=False
                user.groups.add(4)
            print(x)
            return HttpResponseRedirect(reverse('login_master'))
           

    else:
        new_user=Register_empForm()
        return render(request, 'eticket/register_emp.html',{
            "user": new_user
        })


# Profile page for each employee 
@login_required  
def profile_emp(request, emp_id):
    user = User.objects.get(pk=emp_id)
    ticket = Tickets.objects.filter(employee=user).all()
    print(ticket)
    #user_tickets = Problems.objects.filter(pk=user)
    if user is not None:
        return render(request, "eticket/profile_emp.html",{
            "user": user,
            "ticket": ticket            
        })
# profile page for manager
@login_required
def manager_profile(request, user_id):
    tickets = Tickets.objects.all()
    user = User.objects.get(pk=user_id)
    return render(request, "eticket/manager_profile.html",{
        "user": user,
        "all_tickets": tickets
    })
# profile page for it team
@login_required
def it_profile(request, user_id):
    it_user = User.objects.get(pk=user_id)
    return render (request, "eticket/it_profile.html",{
        "user": it_user
    })
# profile page for department manager
@login_required
def dept_mgr_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "eticket/dept_mgr_profile.html",{
        "user": user
    })
# profile page for section manager
@login_required
def sec_mgr_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'eticket/sec_mgr_profile.html',{
        "user": user
    })