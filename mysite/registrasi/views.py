import re
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
    return render(request,'index.html', {'form': form})

def login(request):
    return render(request, 'login.html')

