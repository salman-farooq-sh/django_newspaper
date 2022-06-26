from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from .models import Article, Comment


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'article_list.html'

    def get_queryset(self):
        return Article.objects.order_by('-publication_date')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'


class UserIsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleUpdateView(LoginRequiredMixin, UserIsAuthorMixin, UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_update.html'


class ArticleDeleteView(LoginRequiredMixin, UserIsAuthorMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment']
    template_name = 'comment_create.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['article'] = Article.objects.get(pk=self.request.GET['article'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.request.GET['article'])
        return super().form_valid(form)