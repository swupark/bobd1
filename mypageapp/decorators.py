from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib import messages

from django.shortcuts import redirect

import accountapp


def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(accountapp.login)
        return function(request, *args, **kwargs)
    return wrap