from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("list/", views.list, name="list"),
]
