from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm
from blog.models import Post
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


def home_intorduce(request):
    return render(request, "blog/index.html")


def give_posts(request):
    posts = list(Post.objects.filter(is_published=True).values("id", "title", "price", "publisher"))

    return JsonResponse(posts, safe=False, encoder=DjangoJSONEncoder)


def details(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/details.html", context={"post": post})


def redirect_home(request):
    return redirect("/home")


@login_required
def create_post(request):
    if request.method == "POST":
        post_form = PostForm(
            request.POST,
            request.FILES,
        )

        if post_form.is_valid():
            post_save = post_form.save(commit=False)
            post_save.author = request.user
            post_save.save()

            return redirect("/home")
    else:
        post_form = PostForm()

    return render(request, "blog/postform.html", context={"form": post_form})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        pass
    else:
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )
    return render(request, "blog/postform.html", {"form": form})
