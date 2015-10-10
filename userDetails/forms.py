from django import forms
from django.contrib.auth.models import User
#from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class RegistrationForm(forms.Form):
  name = forms.CharField()
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)  
  password2 = forms.CharField(widget=forms.PasswordInput,
                              label="Confirm password")  
 # captcha = CaptchaField()
  
   
  def clean_password2(self):
    password = self.cleaned_data['password']  
    password2 = self.cleaned_data['password2']
    if password != password2:
      raise forms.ValidationError("Passwords do not match.")
    return password2

  def valid_email(self):
    email_exists=User.objects.filter(email=email).count()
    if email_exists>0:
      raise forms.ValidationError("email already registered")
    return email  