from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Article, Comment, Category


class CommentInline(TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['title', 'publication_date', 'author', 'was_published_recently']
    filter_horizontal = ['categories']
    inlines = [CommentInline]


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
