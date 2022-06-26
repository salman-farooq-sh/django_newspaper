from django.urls import path
from .views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, CommentCreateView


urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('create_comment/', CommentCreateView.as_view(),name='comment_create'),
]