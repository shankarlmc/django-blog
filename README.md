# Create a blog using Django

## What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Steps Involved:

### Create a virtual environment and start the env

```
# Environment creation in linux/mac/windows
# In linux
sudo apt install python3.8-venv (if not installed on linux)
sudo apt install python3.8-venv
python3 -m venv env
# In windows
python -m venv env
# Start Evnironment
env\Scripts\activate (for windows)
source env/bin/activate (for linux)
```

### Install Django and create a first django-project

```
pip install django
django-admin startproject blog
cd blog
```

### File and Directory structure of our project blog

- blog/: root directory is a container for your project.
- manage.py: A command-line utility that lets you interact with this Django project in various ways.
  python manage.py help --commands
- blog/blog/: The inner blog/ directory is the actual Python package for your project.
- blog/**init**.py: An empty file that tells Python that this directory should be considered a Python package.
- blog/settings.py: Settings/configuration for this Django project.
- blog/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- blog/asgi.py: An entry-point for ASGI-compatible web servers to serve your project (Asynchronous Server Gateway Interface)
- blog/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.
  (Web Server Gateway Interface)

### Run Project using runserver command

```
python manage.py runserver
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Create a first django app

```
python manage.py startapp post
```

### Create first models

Here, each model is represented by a class that subclasses django.db.models.Model.
Each model has a number of class variables, each of which represents a database field in the model.

```
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Blog_Post(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
```

### Register post app in settings.py inside INSTALLED_APPS[]

```
'post',
```

### Migrate all the changes

Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.

```
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser account and goto admin dashboard

```
python manage.py createsuperuser
```

### Setup media files and static files

```
# In settins.py
# for static files
STATIC_URL = '/static/'

STATICFILES_DIR = [
    os.path.join(BASE_DIR, "static"),
]
# for media files
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'

# In urls.py
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Create a first views

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World</h1>")
```

### Create custom urls.py inside post app and register into main urls.py

```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
]
```

### Fetch all posts, categories and render in template

```
posts = Blog_Post.objects.all().order_by("-created_at")
categories = Category.objects.all().filter(is_active=True)
feature_post = Blog_Post.objects.all().filter(is_featured=True).order_by("-created_at")[:1]

context = {
    'categories':categories,
    'posts':posts,
}

return render(request, 'post/index.html', context)
```

### Create search and category filter system

```
q = request.GET.get('q',"")
search_category = request.GET.get('category',"")
if not search_category == "":
    posts = Blog_Post.objects.all().filter(
    category__name__icontains=search_category
    ).order_by("-created_at").exclude(is_featured=True)
elif not q == "":
    posts = Blog_Post.objects.all().filter(
    Q(title__icontains=q) |
    Q(author__username__icontains=q)
    ).order_by("-created_at")
    post_count = posts.count()

context = {
    'q':q,
    'search_category':search_category,
}
return render(request, 'post/index.html', context)

```

### Create a pagination and post details

```
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)

    try:
        page_content = paginator.page(page_number)
    except PageNotAnInteger:
        page_content = paginator.page(1)
    except EmptyPage:
        page_content = paginator.page(paginator.num_pages)

    context = {
        'page_content':page_content,
    }
    return render(request, 'post/index.html', context)
```

### Create a authentication app and perform login

### Create a userprofile update page

### Create a post create functionality in frontend

### Update a post from frontend

### Delete a post from frontend

### Goto next and previous post in post details page
