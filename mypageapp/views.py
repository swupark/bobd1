from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView,  ListView
from excel_import.models import FoodModel

# Create your views here.

class MyPageView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'mypageapp/mypage.html'

class InfoDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'mypageapp/detail.html'
    def get(self, request, pk):
        # Ajax 요청에 대한 응답을 리턴
        return render(request, 'mypageapp/detail.html')


class LikeListView(ListView):
    template_name = 'mypageapp/like_list.html'
    def get(self, request, pk):
        # Ajax 요청에 대한 응답을 리턴
        liked_foods = FoodModel.objects.filter(liked_users=request.user)
        context = {'liked_foods': liked_foods}
        return render(request, self.template_name, context)

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

