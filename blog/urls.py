from django.urls import path
from .views import (
    BlogListView,
    BlogDetailedView,
    BlogCreateView,
    BlogEditView,
    DeleteBlogView,
)

urlpatterns = [
    path("proyect/<int:pk>/delete/", DeleteBlogView.as_view(), name="delete_post"),
    path("proyect/<int:pk>/edit/", BlogEditView.as_view(), name="post_edit"),
    path("proyect/new/", BlogCreateView.as_view(), name="post_new"),
    path("proyect/<int:pk>/", BlogDetailedView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="portfolio"),
]
