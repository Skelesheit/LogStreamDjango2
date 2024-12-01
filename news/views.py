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
    blog_list = models.NewsItem.objects.filter(author=user).order_by('-pub_date')
    comment_list = models.Comment.objects.filter(author=user).order_by('-pub_date')
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
    user = request.user
    blog = get_object_or_404(models.NewsItem, pk=pk, author=request.user)  # Только для авторизованного пользователя
    if user.id == blog.author.id:
        blog.delete()
        return redirect('news:blogs')
    return render(request, '400.html', {'message': 'Вы не можете удалять чужую новость'})


@login_required
def edit_blog_form(request, pk):
    blog = models.NewsItem.objects.get(pk=pk)
    return render(request, 'news/blogs/edit_blog.html', {'blog': blog})


@login_required
def edit_blog(request, pk):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        blog = models.NewsItem.objects.get(pk=pk)
        if blog.author == user:
            blog.title = title
            blog.content = content
            if image:
                blog.picture = image
            blog.save()
            return redirect('news:blogs')
        render(request, '400.html', {'message': 'Вы не можете редактировать эту новость'})
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для редактирования новости'})


def view_blog(request, pk):
    blog = get_object_or_404(models.NewsItem, pk=pk)
    comments = blog.comments.all().order_by('-pub_date')
    return render(request, 'news/blogs/view_blog.html', {'blog': blog, 'comments': comments}, )


@login_required
def create_comment(request, pk):
    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        blog = models.NewsItem.objects.get(pk=pk)
        comment = models.Comment.objects.create(author=user, content=content, picture=image, news_item=blog)
        comment.save()
        return redirect('news:view_blog', pk=pk)
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для создания комментариев'})


@login_required
def delete_comment(request, pk):
    user = request.user
    comment = get_object_or_404(models.Comment, pk=pk)
    if user == comment.author:
        comment.delete()
        return redirect('news:blogs')
    return render(request, '400.html', {'message': 'Вы не можете удалять чужой комментарий'})


def get_news(request):
    search_query = request.GET.get('search', '')
    sort_by_date = request.GET.get('sort_by_date', False)
    blogs = models.NewsItem.objects.all()
    print(sort_by_date)
    if search_query:
        blogs = blogs.filter(title__icontains=search_query)
    if not sort_by_date:
        blogs = blogs.order_by('pub_date')
    return render(request, 'news/general/news.html', {'blogs': blogs})
