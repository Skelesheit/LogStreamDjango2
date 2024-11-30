from django.urls import path

from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('edit-profile-email/', views.edit_profile_email, name='edit_profile_email'),
    path('edit-profile-username/', views.edit_profile_username, name='edit_profile_username'),
    path('edit-profile-password/', views.edit_profile_password, name='edit_profile_password'),
]