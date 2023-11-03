from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
#
# class MyAccountManager(BaseUserManager):
#     # 일반 user 생성, username 이 userID를 의미함
#     def create_user(self, username, nickname, password=None):
#         if not username:
#             raise ValueError("Users must have an userID.")
#         if not nickname:
#             raise ValueError("Users must have an name.")
#         user = self.model(
#             username=username,
#             name=nickname
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     # 관리자 User 생성
#     def create_superuser(self, username, nickname, password):
#         user = self.create_user(
#             username=username,
#             name=nickname,
#             password=password
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save()
#         return user


class Account(AbstractBaseUser):
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
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=40, unique=True, blank=False)
    #password = models.CharField( max_length=128,blank=False)
    create_at = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    age = models.IntegerField(choices=age_choices, default=younger)
    gender = models.CharField(max_length=1, choices=gender_choices, default=Female)
    issue_ls = models.IntegerField(choices=choices, default=false)
    issue_hp = models.IntegerField(choices=choices, default=false)
    issue_lk = models.IntegerField(choices=choices, default=false)
    issue_vg = models.IntegerField(choices=choices, default=false)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # object = MyAccountManager()  # 헬퍼 클래스 사용
    #
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    #     self._password = raw_password
    #
    # USERNAME_FIELD = 'username'  # 로그인 ID로 사용할 필드
    # REQUIRED_FIELDS = ['nickname']  # 필수 작성 필드
    #
    # def __str__(self):
    #     return self.username
