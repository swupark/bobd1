from random import shuffle

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

from accountapp.forms import PasswordResetForm
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



def FindIDview(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user is not None:
                template = render_to_string('accountapp/email_template.html', {'nickname':user.userinfo.nickname, 'id':user.username})
                method_email = EmailMessage(
                    'Your ID is in the email',
                    template,
                    settings.EMAIL_HOST_USER,
                    [email],
                    )
                method_email.send(fail_silently=False)
                return render(request, 'accountapp/id_sent.html', context)
        except:
            messages.info(request, "There is no username along with the email")
    context = {}
    return render(request, 'accountapp/find_id.html', context)


class PasswordResetView(auth_views.PasswordResetView):
    """
    비밀번호 초기화 - 사용자ID, email 입력
    """
    template_name = 'accountapp/password_reset.html'
    # success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    # email_template_name = 'common/password_reset_email.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    비밀번호 초기화 - 메일 전송 완료
    """
    template_name = 'accountapp/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    비밀번호 초기화 - 새로운 비밀번호 입력
    """
    template_name = 'accountapp/password_reset_confirm.html'
    success_url = reverse_lazy('accountapp:login')
