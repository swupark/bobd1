from django.urls import path, include
from rest_framework import routers

from likeapp.views import FoodModelViewSet

app_name='likeapp'

router = routers.DefaultRouter()
router.register('like_board', FoodModelViewSet)
urlpatterns=[
    path('', include(router.urls)),
]