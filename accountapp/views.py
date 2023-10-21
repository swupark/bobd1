from django.contrib import auth, messages

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate

from signupapp.models import Account


def homepage(request):
    user_id = request.session.get('user')
    if user_id:
        member = Account.object.get(username=user_id)
        return HttpResponse(member.id)

    return render(request, 'accountapp/home.html')

def Logout(request):
    logout(request)
    return redirect('accountapp:login')


def login(request):
    if request.method == 'GET':
        return render(request, 'accountapp/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 응답 데이터
        res_data = {}

        # 모든 필드를 채우지 않았을 경우
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
            return render(request, 'accountapp/login.html', res_data)

        # 모든 필드를 채웠을 경우
            # 사용자가 보낸 username을 가지고 있는 데이터를 가져온다. authenticate는 username만 체크
        user = authenticate(request, username=username, password=password)
            # 사용자가 보낸 password와 데이터베이스에 저장된 password 일치 여부 확인
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('accountapp:home')
        else:
            messages.error(request, 'ID 혹은 비밀번호 오류입니다.')
            return redirect('signup')
