from django.contrib import admin
from .models import Category, Blog_Post
# Register your models here.


class CategoryAdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)

class PostAdminModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author', 'category','created_at')
    list_filter = ('created_at',)
    list_editable = ('category',)

admin.site.register(Category, CategoryAdminModel)
admin.site.register(Blog_Post, PostAdminModel)