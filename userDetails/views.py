from django.shortcuts import render,redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
import base64
import json
from django.db.models import Q


# Create your views here.

@require_GET
def base(request):
    if request.user.is_authenticated():
        return redirect('home')
    next_url = request.GET.get('next')
    loginform = LoginForm()
    data = { 'loginform' : loginform, 'signupform' : signupform, 'next' : next_url }
    return render(request, 'registration/register.html', data);

@require_POST
def handleLogin(request):
    if request.user.is_authenticated():
        return redirect('bins')
    f = LoginForm(request.POST)
    nexturl = request.POST.get('next')
    if f.is_valid():
        user = f.get_user();
        login(request, user);
        if not nexturl:
            return redirect('hello')
            print("No next url.. redirecting to hello")
        else:
            return redirect(nexturl)
            print("Redirecting to nexturl ... enjoy the show")
    else:
        loginform = f
        data = { 'loginform' : loginform, 'next' : nexturl }
        return render(request, 'account/base.html', data);

def hello(request):
    return HttpResponse("Hello")