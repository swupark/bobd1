"""
URL configuration for bob_d project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.contrib.auth import views as auth_views

import accountapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('accountapp.urls')),
    path('mypage/',include('mypageapp.urls')),
    path('excel_import/', include('excel_import.urls')),
    path('recipes/', include('recipesapp.urls')),
    path('likes/', include('likeapp.urls')),

    path('password_reset/', accountapp.views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', accountapp.views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', accountapp.views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

]
