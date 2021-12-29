from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login', views.fazer_login, name='login')
]