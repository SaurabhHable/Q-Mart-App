from . import views
from django.urls import path

urlpatterns = [
    path("", views.list, name="list"),
    path("home/", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
]
