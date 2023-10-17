from django.shortcuts import render

# Create your views here.

def mypage(request) :
    return render(request, 'mypageapp/mypage.html', {})

def loading(request) :
    return render(request, 'loading.html', {})

