from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<str:slug>', views.details, name="blog-details"),
]
