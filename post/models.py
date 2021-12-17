from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"


    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog_Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"