from django import forms
from django.contrib.auth.models import User
#from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    def valid_user(self):
    	user_exists=User.objects.filter(username=username).count()
    	if user_exists==0:
    		raise forms.ValidationError("username or password invalid")
    	return username 


 