from django.contrib import admin
from .models import Post, PostCategory, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'category', 'pub_date', 'author')
    search_fields = ('title', )
    list_filter = ('pub_date', )
    empty_value_display = "-none-"


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = "-none-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'author')
    search_fields = ('text',)
    empty_value_display = "-none-"