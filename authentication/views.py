from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


# Здесь только логика для аутенфикации. И без каких либо страниц

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
            return redirect('news:profile')
        except IntegrityError as e:
            print("какая то ошибка:")
            print(str(e))
            return render(request, '400.html', {'message': f"Ошибка регистрации: {str(e)}"})
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для регистрации'})


def login(request):
    print("есть ответ?")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
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


@login_required
def logout(request):
    auth.logout(request)
    return redirect('news:index')


@login_required
def edit_profile_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        user = request.user
        errors = list()  # на будущее для других проверок оставлю списком
        if new_password and not user.check_password(current_password):
            errors.append("Текущий пароль неверен.")
        if new_password:
            errors.append("Новый пароль пустой")
        if not errors:
            if new_password:
                user.set_password(new_password)
                # Обновляем сессию, чтобы не разлогинить пользователя
                auth.update_session_auth_hash(request, user)
            user.save()
            messages.success(request, "Ваш профиль успешно обновлён.")
        else:
            for error in errors:
                messages.error(request, error)
        return redirect('news:profile')

    return render(request, '400.html', {'message': 'Только POST запросы разрешены для редактирования профиля'})


@login_required
def edit_profile_username(request):
    if request.method == "POST":
        username = request.POST['username']
        user = request.user
        if username:
            user.username = username
            user.save()
            messages.success(request, "Ваше имя успешно обновлено.")
        else:
            messages.error(request, "Пустое имя пользователя")
        return redirect('news:profile')
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для редактирования профиля'})


@login_required
def edit_profile_email(request):
    if request.method == "POST":
        email = request.POST['email']
        user = request.user
        if email:
            user.email = email
            user.save()
            messages.success(request, "Ваше email успешно обновлён.")
        else:
            messages.error(request, "Пустое имя пользователя")
        return redirect('news:profile')
    return render(request, '400.html', {'message': 'Только POST запросы разрешены для редактирования профиля'})

# мда, такой ужасный код могу писать только я
