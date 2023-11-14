from django.urls import path

from signupapp.views import signup, UserInfoView

app_name='signupapp'

urlpatterns = [
    path('',signup, name='signup'),
    path('info',UserInfoView.as_view(), name='info'),
]