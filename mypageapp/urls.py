from django.urls import path

from mypageapp.views import mypage

app_name='mypageapp'
urlpatterns=[
    path('', mypage, name='mypage'),
]