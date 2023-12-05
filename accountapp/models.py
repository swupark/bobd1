from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    teen = 18
    younger = 29
    middle = 64
    elder = 65

    Male = 'M'
    Female = 'F'

    true = 1
    false = 0

    age_choices = [
        (teen, '청소년(13세 ~ 18세)'),
        (younger, '청년(19세 ~ 29세)'),
        (middle, '중장년(30 ~ 64세)'),
        (elder, '노년(65세 이상 ~)')
    ]
    gender_choices = [
        (Male, '남성'),
        (Female, '여성')
    ]
    choices = [
        (true, '네'),
        (false, '아니오')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')
    nickname = models.CharField(max_length=40, unique=True,null=True)
    age = models.IntegerField(choices=age_choices, default=younger)
    gender = models.CharField(max_length=1, choices=gender_choices, default=Female)
    issue_ln = models.IntegerField(choices=choices, default=false)
    issue_hp = models.IntegerField(choices=choices, default=false)
    issue_vg = models.IntegerField(choices=choices, default=false)
    issue_di = models.IntegerField(choices=choices, default=false)
    is_active = models.BooleanField(default=True)