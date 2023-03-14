from django.urls import path

from . import views

urlpatterns = [
    path("", views.homePageView, name="home"),
    path("", views.index, name="index"),
]
