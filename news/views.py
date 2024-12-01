from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from news import models


# Create your views here.

def index(request):
    news_list = models.NewsItem.objects.order_by('-pub_date')[:3] if models.NewsItem.objects.exists() else []
    title = "Новости"
    return render(request, 'news/general/home.html', context={'news_list': news_list, 'title': title})


def get_contacts(request):
    return render(request, 'news/general/contacts.html')


def login_form(request):
    print("Лол")
    return render(request, 'news/forms/login.html')


def register_form(request):
    return render(request, 'news/forms/register.html')


@login_required
def profile(request):
    print("Попадаем в профиль")
    return render(request, 'news/profile/profile.html')


@login_required
def blogs(request):
    user = request.user
    blog_list = models.NewsItem.objects.filter(author=user).order_by('-pub_date')[:3]
    comment_list = models.Comment.objects.filter(author=user).order_by('-pub_date')[:3]
    return render(request, 'news/blogs/blogs.html',
                  {'blogs': blog_list, 'comments': comment_list})


@login_required
def create_blog_form(request):
    return render(request, 'news/blogs/create_blog.html')


@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        print(image)
        user = request.user
        models.NewsItem(author=user, title=title, content=content, picture=image).save()
        return redirect('news:blogs')
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для создания новости'})


@login_required
def delete_blog(request, pk):
    # Получаем новость по ID
    blog = get_object_or_404(models.NewsItem, pk=pk, author=request.user)  # Только для авторизованного пользователя
    blog.delete()  # Удаляем новость
    return redirect('news:blogs')


@login_required
def edit_blog_form(request, pk):
    blog = models.NewsItem.objects.get(pk=pk)
    return render(request, 'news/blogs/edit_blog.html', {'blog': blog})


@login_required
def edit_blog(request, pk):
    return redirect('news:blogs')


def view_blog(request, pk):
    blog = get_object_or_404(models.NewsItem, pk=pk)
    return render(request, 'news/blogs/view_blog.html', {'blog': blog})
