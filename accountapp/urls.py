
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import homepage, details, FindIDview, CustomLoginView

app_name='accountapp'
urlpatterns=[
    path('login/',CustomLoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', homepage,name='home'),
    path('details/<int:imageId>/', details, name='details'),
    path('find_id', FindIDview, name='findid'),

]