from . import views
from django.urls import path

urlpatterns = [
    path("list/", views.list, name="list"),
    path("", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
]
