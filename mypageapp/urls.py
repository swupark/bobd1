from django.urls import path

from mypageapp.views import MyPageView, InfoDetailView, LikeListView, ReviewListlView, CommentListView

app_name='mypageapp'
urlpatterns=[
    path('<int:pk>/', MyPageView.as_view(), name='mypage'),
    path('<int:pk>/detail/', InfoDetailView.as_view(), name='detail'),
    path('<int:pk>/likelist/', LikeListView.as_view(), name='likelist'),
    path('<int:pk>/reviewlist/', ReviewListlView.as_view(), name='reviewlist'),
    path('<int:pk>/commentlist/', CommentListView.as_view(), name='commentlist'),
]