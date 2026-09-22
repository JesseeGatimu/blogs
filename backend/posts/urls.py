from django.urls import path
from .views import PostListCreateAPI,PostDetailAPI

urlpatterns=[
    path("posts/",PostListCreateAPI.as_view(),name="posts"),
    path("posts/<int:pk>/",PostDetailAPI.as_view(),name="post-detail"),
]