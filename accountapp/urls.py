
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import homepage, details, FindIDview, CustomLoginView, change_pw, AccountDeleteView, \
    UserInfoUpdateView, signup, UserInfoCreateView

app_name='accountapp'
urlpatterns=[
    path('login/',CustomLoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', homepage,name='home'),
    path('details/<int:imageId>/', details, name='details'),
    path('find_id', FindIDview, name='findid'),
    path('pwupdate/<int:pk>', change_pw, name='pwupdate'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('infoupdate/<int:pk>', UserInfoUpdateView.as_view(), name='infoupdate'),
    path('signup/', signup, name='signup'),
    path('infocreate/', UserInfoCreateView.as_view(), name='infocreate'),

]