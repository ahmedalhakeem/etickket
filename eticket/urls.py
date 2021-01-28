from django.urls import path
from . import views
from django.contrib import admin

urlpatterns =[
    path("", views.index, name="index"),
    path("login_manager", views.login_manager, name="login_manager"),
    path("login_dep_mgr", views.login_dep_mgr, name="login_dep_mgr"),
    path("login_sec_mgr", views.login_sec_mgr, name="login_sec_mgr"),
    path("login_it", views.login_it, name="login_it"),
    path("login_emp", views.login_emp, name="login_emp"),
    path("register_emp", views.register_emp, name="register_emp"),
    path("profile_emp/<int:emp_id>", views.profile_emp, name="profile_emp"),
    path("manager_profile", views.manager_profile, name="manager_profile"),
    path("it_profile/<int:user_id>", views.it_profile, name="it_profile")
]
