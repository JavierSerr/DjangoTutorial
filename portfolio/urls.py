from django.urls import path

from .views import PortfolioPageView, PortfolioDetailedView

urlpatterns = [
    path("post/<int:pk>/", PortfolioDetailedView.as_view(), name="post_detail"),
    path("", PortfolioPageView.as_view(), name="blog"),
]
