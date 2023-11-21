from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from signupapp.models import UserInfo


class UserForm(UserCreationForm):

    username = forms.CharField(label="ID")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", )

class UserInfoForm(ModelForm):
    class Meta:
        model=UserInfo
        fields=['nickname','age','gender','issue_ln','issue_hp',
               'issue_vg','issue_di']

