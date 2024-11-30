from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from news import models


# Create your views here.

def index(request):
    news_list = models.NewsItem.objects.order_by('-pub_date')[:3] if models.NewsItem.objects.exists() else []
    title = "Новости"
    return render(request, 'news/home.html', context={'news_list': news_list, 'title': title})


def get_contacts(request):
    return render(request, 'news/contacts.html')


def login_form(request):
    print("Лол")
    return render(request, 'news/login.html')


def register_form(request):
    return render(request, 'news/register.html')


@login_required
def profile(request):
    print("Попадаем в профиль")
    return render(request, 'news/profile.html')


@login_required
def blogs(request):
    blog_list = models.NewsItem.objects.order_by('-pub_date')
    return render(request, 'news/blogs.html', {'blogs': blog_list})


@login_required
def edit_blog_form(request, blog_id):
    return render(request, 'news/edit_blog.html', {'blog_id': blog_id})


@login_required
def edit_blog(request, blog_id):
    pass


@login_required
def create_blog_form(request):
    return render(request, 'news/create_blog.html')


@login_required
def create_blog(request):
    pass
