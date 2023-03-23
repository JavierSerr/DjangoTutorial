from django.urls import path
from .views import (
    BlogListView,
    BlogDetailedView,
    BlogCreateView,
    BlogEditView,
    DeleteBlogView,
)

urlpatterns = [
    path("post/<int:pk>/delete/", DeleteBlogView.as_view(), name="delete_post"),
    path("post/<int:pk>/edit/", BlogEditView.as_view(), name="post_edit"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailedView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="blog"),
]
