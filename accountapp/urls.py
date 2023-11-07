
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
app_name='accountapp'
urlpatterns=[
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/',views.homepage,name='home'),
    path('details/<int:imageId>/', views.details, name='details'),

]