import imp
from multiprocessing import context
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Internal permission check
def index(request):
    context = {
        'halaman' : 'Home',
        'deskripsi' : 'Ini halaman home',
    }
    
    template_name = None
    if request.user.is_authenticated:
        # logika untuk user
        template_name = 'index_user.html'
    else:   
        # logika untuk anonymous
        template_name = 'index_anonymous.html'

    return render(request, template_name, context)

def about(request):
    context = {
        'halaman' : 'about',
        'deskripsi'  :'ini about'
    }
    return render(request, 'about.html', context)

def loginView(request):
    context = {
        'page_title':'LOGIN',
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(index)
        else:
            return render(request, 'login.html', context)

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request,username = username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            return redirect('login')

        
    return render(request, 'login.html', context)

@login_required
def logoutView(request):
    context = {
        'page_title':'logout',
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
            
        return redirect(index)

    return render(request, 'logout.html', context)
	

