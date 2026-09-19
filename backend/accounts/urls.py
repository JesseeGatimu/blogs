from django.urls import path, include
from .views import LoginAPI,RegisterAPI,LogoutAPI

url_patterns=[
    path("register/",RegisterAPI.as_view(),name="register"),
    path("login/",LoginAPI.as_view(),name="login"),
    path("logout/",LogoutAPI.as_view(),name="logout"),
]