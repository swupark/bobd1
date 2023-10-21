from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from signupapp.models import Account


def homepage(request):
#    user_id = request.session.get('user')
#    if user_id:
#        member = Account.object.get(username=user_id)
#        return HttpResponse(member.id)

    return render(request, 'accountapp/home.html')


def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('/account/home')


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

        # 모든 필드를 채웠을 경우
        else:

            # 사용자가 보낸 username을 가지고 있는 데이터를 가져온다.
            # 일치하는 데이터가 없을 때 예외처리 (get_object_or_404)
            user = Account.object.get(username=username)

            # 사용자가 보낸 password와 데이터베이스에 저장된 password 일치 여부 확인
            # check_password 로 hash화 되어있는 비밀번호를 대조하기
            if (password==user.password):

                # 비밀번호가 일치하면 session을 사용해 user.id 를 넘겨준다.
                request.session['user'] = user.username

                return redirect('/account/home')
            # 비밀번호가 일치하지 않으면 에러
            else:
                res_data['error'] = '비밀번호가 일치하지 않습니다'

        # 로그인 실패 및 오류메세지와 함께 응답
    return redirect(request,'/account/login',res_data)
