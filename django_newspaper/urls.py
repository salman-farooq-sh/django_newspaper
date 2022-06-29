from django.contrib import admin
from django.templatetags.static import static
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url=static('icons/news_icon_3_white.png'))),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
