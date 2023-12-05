from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib import messages

from django.shortcuts import redirect

import accountapp


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated