from django.contrib import admin
from django.urls import path, include
from .views import UserRegistrationView, login, logout, user_profile, IndexView



app_name = 'users'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='profile'),
]

