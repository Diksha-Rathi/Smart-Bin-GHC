from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.core import serializers
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, Http404
import base64
import requests
from .forms import LoginForm

def hello(request):
    return HttpResponse("Hello")


def myLogin(request):
  if(request.user.is_authenticated()):
    print("User authenticated tada..")
    return redirect('/bins')
  if (request.method == 'GET'):
    print("GET request activated ..")
    form = LoginForm()
    next_url = request.GET.get('next', '')
    return render(request, 'index.html', {'form' : form ,'next': next_url})
  if (request.method == 'POST'):
    print("Post request activated ..")
    next_url = request.POST.get('next', '')
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username= username, password = password)
      if user is not None:
        login(request, user)
        if next_url :
          print("Next url activated")
          return redirect(next_url)
        else:
          print("Next url not there")
          return redirect('/bins')
      else:
        print ("Invalid User")
        return redirect('/login/') 
    else:
      loginform=form
      data={'loginform':loginform,'next':next_url}
      return render(request,'index.html',data)      

@require_GET
def logoutview(request):
    logout(request)
    return redirect('/login')
 