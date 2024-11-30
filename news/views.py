from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from news import models


# Create your views here.

def index(request):
    news_list = models.NewsItem.objects.order_by('-pub_date')[:3] if models.NewsItem.objects.exists() else []
    title = "Новости"
    return render(request, 'news/home.html', context={'news_list': news_list, 'title': title})


def login_form(request):
    print("Лол")
    return render(request, 'news/login.html')


def login(request):
    print("есть ответ?")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                print("вошли в профиль")
                messages.success(request, 'Валидация прошла успешно!')
                return redirect('news:profile')
            else:
                messages.error(request, "Неверное имя пользователя или пароль")
                print("Пользователь не прошёл авторизацию")
                return redirect('news:login_form')
        except Exception as e:
            print("какая то ошибка:")
            print(str(e))
            return render(request, '400.html', {'message': f"Ошибка авторизации: {str(e)}"})
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для регистрации'})


def register_form(request):
    return render(request, 'news/register.html')


def register(request):
    print("Я здесь!")
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            auth.login(request, user)
            print("Профиль создан")
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('news:profile')
        except IntegrityError as e:
            print("какая то ошибка:")
            print(str(e))
            return render(request, '400.html', {'message': f"Ошибка регистрации: {str(e)}"})
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для регистрации'})


@login_required
def profile(request):
    print("Попадаем в профиль")
    return render(request, 'news/profile.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('news:index')
