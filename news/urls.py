from django.urls import path

from news import views
app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_form', views.login_form, name='login_form'),
    path('login', views.login, name='login'),
    path('register_form', views.register_form, name='register_form'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),

]