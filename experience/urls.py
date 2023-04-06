from django.urls import path

from .views import HomePageView, AboutPageView, ExperiencePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("experience/", ExperiencePageView.as_view(), name="experience"),
]
