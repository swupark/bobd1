from django.forms import ModelForm

from signupapp.models import UserInfo


class UserInfoForm(ModelForm):
    class Meta:
        model=UserInfo
        fields=['nickname','age','gender','issue_ls','issue_hp',
               'issue_lk','issue_vg']

