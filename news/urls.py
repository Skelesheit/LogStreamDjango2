from django.urls import path

from news import views
app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_form/', views.login_form, name='login_form'),
    path('register_form/', views.register_form, name='register_form'),
    path('profile/', views.profile, name='profile'),
    path('blogs/', views.blogs, name='blogs'),
    path('edit-blog/', views.edit_blog, name='edit_blog'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('contacts', views.get_contacts, name='contacts')
]