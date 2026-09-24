from django.urls import path
from .views import home_intorduce, redirect_home, give_posts, details

app_name = "blog"

urlpatterns = [
    path("home", home_intorduce, name="home"),
    path("", redirect_home, name="home_redirect"),
    path("api/posts", give_posts, name='give_published_posts'),
    path("posts/<int:id>", details, name="post_details")
]
