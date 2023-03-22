from django.urls import path
from .views import BlogListView, BlogDetailedView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailedView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="blog"),
]
