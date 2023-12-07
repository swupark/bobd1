from django.urls import path

from mypageapp.views import MyPageView, InfoDetailView, LikeListAPIView, ReviewListlView, CommentListView

app_name='mypageapp'
urlpatterns=[
    path('<int:pk>/', MyPageView.as_view(), name='mypage'),
    path('<int:pk>/detail/', InfoDetailView.as_view(), name='detail'),
    path('<int:pk>/likelist/', LikeListAPIView.as_view(), name='likelist'),
    path('<int:pk>/reviewlist/', ReviewListlView.as_view(), name='reviewlist'),
    path('<int:pk>/commentlist/', CommentListView.as_view(), name='commentlist'),
]