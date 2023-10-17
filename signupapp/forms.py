from django.forms import ModelForm
from django import forms

from signupapp.models import Account


class SignuppForm(ModelForm):
    class Meta:
        model=Account
        fields=['nickname','username','password','age','gender','issue_ls','issue_hp',
               'issue_lk','issue_vg']

