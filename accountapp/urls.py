
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
from myapp.views import Predict

app_name='accountapp'
urlpatterns=[
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/',views.homepage,name='home'),
    # path('train-doc2vec-model/<int:imageId>/<str:category>', TrainDoc2VecModel.as_view(), name='train-doc2vec-model'),
    path('list/<int:imageId>/<str:category>', Predict.as_view(), name='list'),

]