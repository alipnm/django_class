from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm
from blog.models import Post
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json


def home_intorduce(request):
    return render(request, "blog/index.html")


def give_posts(request):
    posts = list(Post.objects.filter(is_published=True).values(
        'id', 'title', 'price', 'publisher'
    ))

    return JsonResponse(posts, safe=False, encoder=DjangoJSONEncoder)

def details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/details.html', context={'post': post})

def redirect_home(request):
    return redirect('/home')


@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(
            request.POST,
            request.FILES,
        )
        
        if post_form.is_valid():
            post_save = post_form.save(commit=False)
            post_save.author = request.user
    else:
        pass
