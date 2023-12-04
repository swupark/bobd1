from django.urls import path

from likeapp.views import toggle_like, check_like_status
from .views import menu_detail

urlpatterns = [
    path('menu/<int:food_id>/', menu_detail, name='menu_detail'),
    path('menu/<int:food_id>/like/', toggle_like, name='api_toggle_like'),
    path('menu/<int:food_id>/like-status/', check_like_status, name='api_like_status'),
    # 다른 URL 패턴 추가
]