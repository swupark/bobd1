
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
app_name='accountapp'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('home/',views.homepage,name='home'),
    path('logout/',views.logout,name='logout'),
]