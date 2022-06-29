from datetime import timedelta

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{reverse("article_list")}?categories={self.id}'


class Article(models.Model):
    class Meta:
        ordering = ['-publication_date']

    title = models.CharField(max_length=255)
    body = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(to=Category)
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.pk])

    @admin.display(
        boolean=True,
        ordering='publication_date',
        description='Published Recently?',
    )
    def was_published_recently(self):
        return now() - timedelta(days=3) < self.publication_date


class Comment(models.Model):
    comment = models.TextField()
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.article.pk])
