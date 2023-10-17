from django.urls import path

from mypageapp.views import mypage, loading

app_name='mypageapp'
urlpatterns=[
    path('', mypage, name='mypage'),
    path('loading', loading, name='loading'),
]