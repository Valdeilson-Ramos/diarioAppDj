from django import forms
from django.forms.forms import Form

class LoginForm(forms.Form):
    username=forms.CharField(max_length=11)
    password=forms.CharField(max_length=30, widget=forms.PasswordInput)
