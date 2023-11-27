from random import shuffle

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from django.conf import settings

from accountapp.forms import PasswordResetForm, CustomAuthenticationForm
from excel_import.models import FoodModel

def homepage(request):
    vegan_img = list(FoodModel.objects.filter(VEGAN=1).all())
    hp_img = list(FoodModel.objects.filter(HIGH_PRO=1).all())
    ln_img = list(FoodModel.objects.filter(LOW_NA=1).all())
    dt_img = list(FoodModel.objects.filter(DIETS=1).all())
    # vegan = list(FoodModel.objects.values('VEGAN'))
    # vegan = list(FoodModel.objects.values('VEGAN'))
    # vegan = list(FoodModel.objects.values('VEGAN'))
    # vegan = list(FoodModel.objects.values('VEGAN'))
    shuffle(vegan_img)
    shuffle(hp_img)
    shuffle(ln_img)
    shuffle(dt_img)
    return render(request, 'accountapp/home.html',{'vegan_img': vegan_img, 'hp_img': hp_img, 'ln_img': ln_img, 'dt_img': dt_img})
def details(request,imageId):
    rcp = get_object_or_404(FoodModel, id=imageId)
    return render(request,'accountapp/details.html',{'post':imageId, 'rcp':rcp})

def dislike(dislike_igt):
    # 싫어하는 재료를 입력받습니다.
    dislike_ingredient = dislike_igt

    # 모든 레시피를 가져옵니다.
    vegan_img = list(FoodModel.objects.filter(VEGAN=1).all())
    hp_img = list(FoodModel.objects.filter(HIGH_PRO=1).all())
    ln_img = list(FoodModel.objects.filter(LOW_NA=1).all())
    dt_img = list(FoodModel.objects.filter(DIETS=1).all())

    # 사용자가 입력한 싫어하는 재료가 있을 경우 해당하는 레시피를 제거합니다.
    if dislike_ingredient:
        vegan_img = [recipe for recipe in vegan_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
        hp_img = [recipe for recipe in hp_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
        ln_img = [recipe for recipe in ln_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
        dt_img = [recipe for recipe in dt_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]

    # 레시피 리스트를 섞습니다.
    shuffle(vegan_img)
    shuffle(hp_img)
    shuffle(ln_img)
    shuffle(dt_img)

    return (vegan_img,  hp_img,  ln_img, dt_img)

class CustomLoginView(auth_views.LoginView):
    form_class = CustomAuthenticationForm

#아이디 찾기
def FindIDview(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user is not None:
                template = render_to_string('accountapp/email_template.html', {'nickname':user.userinfo.nickname, 'id':user.username})
                method_email = EmailMessage(
                    'Your ID is in the email', #메일 제목
                    template, #메일 내용 html
                    settings.EMAIL_HOST_USER, #메일 보내는 사람
                    [email],
                    )
                method_email.send(fail_silently=False) #메일 보내는 동안 오류 발생해도 무시하고 보냄
                return render(request, 'accountapp/id_sent.html', context) #메일 발송 시 성공 페이지로 연결
        except:
            messages.info(request, "해당 이메일로 가입한 아이디가 존재하지 않습니다.")
    context = {}
    return render(request, 'accountapp/id_find.html', context)

#비밀번호 찾기 (사용자ID, email 입력)
class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'accountapp/password_reset.html'
    # success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    # email_template_name = 'common/password_reset_email.html'

#비밀번호 찾기 (메일 전송 완료)
class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accountapp/password_reset_done.html'

#비밀번호 찾기 (새로운 비밀번호 입력)
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accountapp/password_reset_confirm.html'
    success_url = reverse_lazy('accountapp:login')
