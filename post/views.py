from django.contrib import messages
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Blog_Post
from django.db.models.aggregates import Count
from django.core.paginator import Paginator
from django.db.models import Q
from next_prev import next_in_order, prev_in_order
from .forms import createPostForm
from django.contrib.auth.decorators import login_required
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


@login_required(login_url="/login")
def createPost(request):
    categories = Category.objects.all().filter(is_active=True)
    form = createPostForm()
    if request.method == "POST":
        title = request.POST.get('title')
        if title == "":
            messages.error(request, "Title field is required.")
            return HttpResponseRedirect('/create-post')
        category = Category.objects.get(id=request.POST.get('category'))   
        content = request.POST.get('content')
        if content == "":
            messages.error(request, "Content field is required.")
            return HttpResponseRedirect('/create-post')
        image = request.FILES.get('image')
        if image == "":
            messages.error(request, "Image field is required.")
            return HttpResponseRedirect('/create-post')

        is_active = request.POST.get('is_active')
        is_featured = request.POST.get('is_featured')

        if is_active == "on":
            is_active = True
        else:
            is_active = False

        if is_featured == "on":
            is_featured = True
        else:
            is_featured = False

        post = Blog_Post.objects.create(
            title = title,
            category = category,
            author = request.user,
            content = content,
            image = image,
            is_active = is_active,
            is_featured = is_featured,
        )
        post.save()
        messages.success(request, f"{title} is Created Successfully.")
        return HttpResponseRedirect('/create-post')

    context = {
        'form':form,
        'categories':categories,
    }
    return render(request, 'post/create-post.html', context)


@login_required(login_url="/login")
def editPost(request, slug):
    post = Blog_Post.objects.get(slug=slug)
    if request.method == "POST":
        form = createPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        messages.success(request, "Post Updated Successfully.")
        return HttpResponseRedirect('/profile')
    else:
        form = createPostForm(instance=post)

    context = {
        'form':form,
        'editable_post':post,
    }
    return render(request, 'post/edit-post.html', context)

@login_required(login_url='/login')
def deletePost(request, slug):
    post = Blog_Post.objects.get(slug=slug)
    post.delete()
    messages.success(request, "Post Deleted Successfully.")
    return HttpResponseRedirect('/profile')