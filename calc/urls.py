from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('main',views.main,name="main")
]