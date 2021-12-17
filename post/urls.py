from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<str:slug>', views.details, name="blog-details"),
    path('create-post/', views.createPost, name="create-post"),
    path('update/<str:slug>', views.editPost, name="update"),
    path('delete/<str:slug>', views.deletePost, name="delete"),
]
