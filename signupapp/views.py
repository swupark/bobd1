from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse
from signupapp.forms import SignuppForm
from signupapp.models import Account


#from signupapp.models import Member



class Signupview(CreateView):
        model = Account
        form_class = SignuppForm
        template_name = 'signupapp/signup.html'

        def get_success_url(self):
            return reverse('accountapp:login')
