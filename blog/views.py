from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm


def home_intorduce(request):
    return render(request, "blog/index.html")


def redirect_home(request):
    return redirect('home/')

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
