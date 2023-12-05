from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

# from signupapp.decorators import account_ownership_required
from signupapp.forms import UserInfoForm, UserForm
from signupapp.models import UserInfo

# has_ownership = [account_ownership_required, login_required]

#class SignupView(CreateView):
#    model = User  # 장고 기본 제공 모델
#    form_class = UserCreationForm
#    context_object_name = 'target_user'
#    template_name = 'signupapp/signup.html'
#    success_url = reverse_lazy('signupapp:info')
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()        # 반환값 받아서 user에 저장
            auth_login(request, user) # 반환값 user를 인자로 auth_login() 해서 바로 로그인
            return redirect('signupapp:info')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'signupapp/signup.html', context)
class UserInfoCreateView(CreateView):
    model = UserInfo
    form_class = UserInfoForm
    context_object_name = 'target_userinfo'
    success_url = reverse_lazy('accountapp:home')
    template_name = 'signupapp/info.html'
    def form_valid(self, form):
        info = form.save(commit=False)
        info.user = self.request.user
        info.save()
        return super().form_valid(form)
