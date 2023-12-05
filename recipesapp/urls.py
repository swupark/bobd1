from django.urls import path

from . import views
from .views import Predict

# from .views import menu_list
appname='recipesapp'
urlpatterns = [
    path('menu/<int:imageId>/<str:category>', views.menu_detail, name='menu_detail'),
    # path('list/', menu_list, name='menu_list'),
]