import os

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_newspaper.settings')
django.setup()

from articles.models import Article, Category, Comment

fake = Faker()

if True:
    print(Article.objects.all())
    print(Category.objects.all())
    print(Comment.objects.all())
