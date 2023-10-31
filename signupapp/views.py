from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
#from signupapp.forms import SignuppForm
from signupapp.models import Account




class Signupview(CreateView):
    model = User  # 장고 기본 제공 모델
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:home')  # class에서 리버스를 그대로 사용할 수 없음.
    template_name = 'signupapp/signup.html'
