from django.urls import path

from signupapp.views import signup, UserInfoCreateView

app_name='signupapp'

urlpatterns = [
    path('',signup, name='signup'),
    path('info',UserInfoCreateView.as_view(), name='info'),
]