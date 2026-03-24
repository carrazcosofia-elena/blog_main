from django.contrib import admin

# Register your models here.
from .models import Comment, Category, Post

class CommentItemInline(admin.TabularInline):
    model = Commentraw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ('title', 'category', 'created_at', 'status')
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]


class CategoryAdmin(admin.ModelAdmin):
  search_fields = ['title']
  list_display = ('title')

class CommentAdmin(admin.ModelAdmin):
   list_display = ('name', 'post', 'created_at')

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

