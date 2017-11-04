from django.conf import settings
from django.contrib import messages
#from .forms import AdicionarUsuarioForm
from datetime import *
from django.shortcuts import render, redirect


def home (request):
    template_name = 'dashboard.html'
    


    
    return render(request, template_name)



def dashboard (request):
    template_name = 'dashboard.html'

    
    
    return render(request, template_name)