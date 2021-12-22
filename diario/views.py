from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def index (request):
    return render(request, 'diario/login.html')