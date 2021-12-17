# Create a blog using Django

## Steps Involved:

- Create a virtual environment and start the env

```
python -m venv env
env\Scripts\Activate
```

- Install Django and create a first django-project

```
pip install django
django-admin startproject blog
cd blog
```

- Run Project using runserver command

```
python manage.py runserver
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

- Create a first django app

```
python manage.py startapp post
```

- Create first models

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

- Register post app in settings.py inside INSTALLED_APPS[]

- Migrate all the changes

```
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser account and goto admin dashboard

```
python manage.py createsuperuser
```

- Setup media files and static files

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

- Create a first views

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World</h1>")
```

- Create custom urls.py inside post app and register into main urls.py

```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
]
```

- Fetch all posts, categories and render in template
- Create search and category filter system
- Create a pagination and post details
- Create a authentication app and perform login
- Create a userprofile update page
- Create a post create functionality in frontend
- Update a post from frontend
- Delete a post from frontend
- Goto next and previous post in post details page
