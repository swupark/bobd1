from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.hashers import check_password


#from mypageapp.decorators import account_ownership_required
from django.contrib.auth.decorators import login_required


#has_ownership = [account_ownership_required, login_required]
# Create your views here.

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'mypageapp/mypage.html'

def change_pw(request,pk):
    context = {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                return redirect("accountapp:home")

    return render(request,"mypageapp/update.html")


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:home')
    template_name = 'mypageapp/delete.html'