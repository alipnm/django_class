from django.urls import path
from .views import home_intorduce, redirect_home

app_name = "blog"

urlpatterns = [
    path("home/", home_intorduce, name="home"),
    path("", redirect_home, name="home_redirect")
]
