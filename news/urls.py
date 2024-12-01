from django.urls import path

from news import views
app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_form/', views.login_form, name='login_form'),
    path('register_form/', views.register_form, name='register_form'),
    path('profile/', views.profile, name='profile'),
    path('blogs/', views.blogs, name='blogs'),
    path('create_blog_form/', views.create_blog_form, name='create_blog_form'),
    path('create_blog', views.create_blog, name='create_blog'),
    path('view_blog/<int:pk>/', views.view_blog, name='view_blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('edit_blog_form/<int:pk>/', views.edit_blog_form, name='edit_blog_form'),
    path('edit_blog/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('contacts/', views.get_contacts, name='contacts'),
    path('create_comment/<int:pk>/', views.create_comment, name='create_comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
]