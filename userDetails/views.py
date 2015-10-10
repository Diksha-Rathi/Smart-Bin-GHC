from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
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
from .forms import RegistrationForm,LoginForm

 
def registration_form(request):
  # If the request method is POST, it means that the form has been submitted
  # and we need to validate it.
  if request.method == 'POST':
     
    form = RegistrationForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      print(name,username,password,email)
      if username and password and email and name:
        print("all valid")
        user = User.objects.create_user(username= username, password = password,email=email,first_name=name)
        user.is_active=False
        a=bytes(username,'utf-8')
        encoded=base64.b64encode(a)
        decoded=encoded.decode('utf-8')
        subject='Thank you for registering'
        print("sending email ...")
        message='Please click on the link to activate the account \n'+'127.0.0.1:8000/'+'email_confirmation/'+decoded
        from_email=settings.EMAIL_HOST_USER
        to_list=[email,'tanvisurana2012@gmail.com']
        send_mail(subject,message,settings.EMAIL_HOST_USER,to_list,fail_silently=True)
        user.save()          
        return render(request, "registration/success.html")
      else:
        print('Invalid user redirecting ... to admin..')
        return redirect('/admin/')
  else:
   form = RegistrationForm()
  return render(request, "registration/registration_form.html",
                { "form" : form })


def email_confirmation(request,auth_token):
    x=auth_token
    byte_x=bytes(x,'utf-8')
    encoded=base64.b64decode(byte_x)
    z=encoded.decode('utf-8')
    user=User.objects.get(username=z)
    print(user)
    if user is not None:
        print('activating user')
        user.is_active=True
        user.save()
        return redirect('/admin/')
    else:
        print('Failed to activate')
        return redirect('/register/')     

def hello(request):
    return HttpResponse("Hello")


def myLogin(request):
  if(request.user.is_authenticated()):
    return redirect('/hello')
  if (request.method == 'GET'):
    form = LoginForm()
    next_url = request.GET.get('next', '')
    return render(request, 'registration/registration_form.html', {'form' : form ,'next': next_url})
  if (request.method == 'POST'):
    next_url = request.POST.get('next', '')
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username= username, password = password)
      if user is not None:
        login(request, user)
      if next_url :
        return redirect(next_url)
      else:
        return redirect('/hello')
    else:
      print ("Invalid User")
      return redirect('/register/')   
