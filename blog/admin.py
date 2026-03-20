from django.contrib import admin

# Register your models here.
from .models import Comment, Category, Post

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

