from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Article, Comment


class CommentInline(TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['title', 'publication_date', 'author', 'was_published_recently']
    inlines = [CommentInline]
    ordering = ['-publication_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
