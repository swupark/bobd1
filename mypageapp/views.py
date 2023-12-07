from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView,  ListView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from accountapp.decorators import account_ownership_required
from excel_import.models import FoodModel
from likeapp.serializers import FoodSerializer


# Create your views here.
@method_decorator(login_required, name='dispatch')
@method_decorator(account_ownership_required, name='dispatch')
class MyPageView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'mypageapp/mypage.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(account_ownership_required, name='dispatch')
class InfoDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'mypageapp/detail.html'
    def get(self, request, pk):
        # Ajax 요청에 대한 응답을 리턴
        return render(request, 'mypageapp/detail.html')

class ReviewListlView(ListView):
    template_name = 'mypageapp/review_list.html'
    def get(self, request, pk):
        # Ajax 요청에 대한 응답을 리턴
        return render(request, 'mypageapp/review_list.html')
class CommentListView(ListView):
    template_name = 'mypageapp/comment_list.html'
    def get(self, request, pk):
        # Ajax 요청에 대한 응답을 리턴
        return render(request, 'mypageapp/comment_list.html')

def loading(request) :
    return render(request, 'loading.html', {})

@method_decorator(login_required, name='dispatch')
@method_decorator(account_ownership_required, name='dispatch')
class LikeListAPIView(ListAPIView):
    serializer_class = FoodSerializer
    template_name = 'mypageapp/like_list.html'

    @transaction.atomic
    def get_queryset(self):
        user_id = self.kwargs['pk']
        # user_id에 해당하는 유저의 좋아하는 레시피들을 가져오기
        user_liked_recipes = FoodModel.objects.filter(liked_users=user_id)
        return user_liked_recipes

    def list(self, request, *args, **kwargs):
        user_id = self.kwargs['pk']
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        context = {
            'user_id': user_id,
            'liked_recipes': serializer.data
        }
        return render(request, self.template_name, context)
