from django import forms
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm

from accountapp.models import UserInfo


class UserForm(auth_forms.UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('이미 등록된 아이디입니다.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 등록된 이메일입니다.')
        return email

class UserInfoForm(ModelForm):

    class Meta:
        model=UserInfo
        fields=['nickname','age','gender','issue_ln','issue_hp',
               'issue_vg','issue_di']

class CustomAuthenticationForm(auth_forms.AuthenticationForm):
    error_messages = {
        'required': "빈 칸을 채워주세요.",
        'invalid_login': (
            "아이디가 존재하지 않거나 비밀번호가 틀렸습니다. 다시 입력해 주세요."
        ),
        'inactive': ("이 계정은 인증되지 않았습니다. 인증을 먼저 진행해 주세요."),
    }

    def __init__(self, request=None, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)  # 꼭 있어야 한다!
        self.fields['username'].label = '아이디'
        self.fields['password'].label = '비밀번호'


class PasswordResetForm(auth_forms.PasswordResetForm):
    username = auth_forms.UsernameField(label="사용자ID")  # CharField 대신 사용

    # validation 절차:
    # 1. username에 대응하는 User 인스턴스의 존재성 확인
    # 2. username에 대응하는 email과 입력받은 email이 동일한지 확인

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(username=data).exists():
            raise ValidationError("해당 사용자ID가 존재하지 않습니다.")

        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email:
            if User.objects.get(username=username).email != email:
                raise ValidationError("사용자의 이메일 주소가 일치하지 않습니다")

    def get_users(self, email=''):
        active_users = User.objects.filter(**{
            'username__iexact': self.cleaned_data["username"],
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password()
        )
