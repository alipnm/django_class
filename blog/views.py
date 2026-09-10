from django.shortcuts import render, redirect


def home_intorduce(request):
    return render(request, "blog/index.html")


def redirect_home(request):
    return redirect('home/')
