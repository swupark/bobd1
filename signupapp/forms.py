from django.forms import ModelForm

from signupapp.models import Account


class SignuppForm(ModelForm):
    class Meta:
        model=Account
        fields=['age','gender','issue_ls','issue_hp',
               'issue_lk','issue_vg']

