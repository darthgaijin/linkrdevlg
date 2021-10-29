
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/@<str:pk>/', views.userProfile, name='user-profile'),
    path('user/edit/', views.updateProfile, name='edit-profile'),
    path('user/profile/', views.userProfileMain, name='profile-main'),
    path('discover/', views.allUsers, name='all-users'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.registerUser, name='signup'),
]