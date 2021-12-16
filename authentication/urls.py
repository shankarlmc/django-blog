from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginUser, name="login"),
    path('profile', views.userProfile, name="profile"),
    path('logout', views.logoutUser, name="logout"),
]
