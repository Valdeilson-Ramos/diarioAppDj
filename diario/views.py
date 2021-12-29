from django.shortcuts import render

import diario
from .forms import LoginForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .models import Diario

# Create your views here.
def index (request):
    diario = Diario.objects.all()
    context={
        'diario':diario,
    }
    return render(request, 'diario/index.html', context)

def fazer_login (request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                return HttpResponse('<h1>Olá {} </h1>' .format(user))
            else:
                return HttpResponse('<h1> Usuário ou senha incorreta </h1')
    form=LoginForm()
    context={
        'form':form
    }
    return render(request, 'diario/login.html', context)