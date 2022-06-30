from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from furl import furl

from .forms import ArticleCreateForm, ArticleUpdateForm, CategorySelectForm
from .models import Article, Comment


def add_get_parameter(url, parameter):
    parameter_name, parameter_value = parameter.split('=', maxsplit=2)
    f = furl(url)
    f.args[parameter_name] = parameter_value
    return f.url


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['form'] = CategorySelectForm(
            initial={
                'categories': self.request.GET.getlist('categories'),
            },
        )

        request_url = self.request.get_full_path(force_append_slash=True)
        page_obj = context['page_obj']
        context['page_urls'] = {
            'first': add_get_parameter(
                request_url, f'page=1'
            ),
            'previous': add_get_parameter(
                request_url, f'page={page_obj.previous_page_number() if page_obj.has_previous() else ""}'
            ),
            'next': add_get_parameter(
                request_url, f'page={page_obj.next_page_number() if page_obj.has_next() else ""}'
            ),
            'last': add_get_parameter(
                request_url, f'page={page_obj.paginator.num_pages}'
            ),
        }

        return context

    def get_queryset(self):
        selected_categories = self.request.GET.getlist('categories')
        if selected_categories:
            return Article.objects.filter(categories__in=selected_categories).distinct()
        else:
            return super().get_queryset()


class MyArticleListView(LoginRequiredMixin, ArticleListView):
    template_name = 'my_article_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'


class UserIsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleUpdateView(LoginRequiredMixin, UserIsAuthorMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateForm
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
