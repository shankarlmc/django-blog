from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Category, Blog_Post
from django.db.models.aggregates import Count
from django.core.paginator import Paginator
from django.db.models import Q
from next_prev import next_in_order, prev_in_order
# from django.http import HttpResponse
# Create your views here.

def index(request):
    search_category = request.GET.get('category',"")
    q = request.GET.get('q',"")

    if not search_category == "":
        posts = Blog_Post.objects.all().filter(
        category__name__icontains=search_category
        ).order_by("-created_at").exclude(is_featured=True)
        post_count = posts.count()
    elif not q == "":
        posts = Blog_Post.objects.all().filter(
        Q(title__icontains=q) | 
        Q(author__username__icontains=q)
        ).order_by("-created_at")
        post_count = posts.count()
    else:
        posts = Blog_Post.objects.all().order_by("-created_at").exclude(is_featured=True)
        post_count = posts.count()
    
    categories = Category.objects.all().filter(is_active=True)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    
    try:
        page_content = paginator.page(page_number)
    except PageNotAnInteger:
        page_content = paginator.page(1)
    except EmptyPage:
        page_content = paginator.page(paginator.num_pages)

    feature_post = Blog_Post.objects.all().filter(is_featured=True).order_by("-created_at")[:1]

    context = {
        'search_category':search_category,
        'categories':categories,
        'page_content':page_content,
        'feature_post':feature_post,
        'q':q,
        'post_count':post_count
    }
    return render(request, 'post/index.html', context)

def details(request, slug):
    categories = Category.objects.annotate(num_posts=Count('blog_post')).filter(is_active=True)
    post = Blog_Post.objects.get(slug=slug)
    previous_post = prev_in_order(post)
    next_post = next_in_order(post)

    context = {
        'post':post,
        'categories':categories,
        'previous_post':previous_post,
        'next_post':next_post,
    }
    return render(request, 'post/post-details.html', context)
