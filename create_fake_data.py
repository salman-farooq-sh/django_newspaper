import os
from random import choice, sample

import django
from django.contrib.auth import get_user_model
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_newspaper.settings')
django.setup()

from articles.models import Article, Category, Comment

fake = Faker()

for _ in range(1):
    a = Article(
        title=fake.sentence(nb_words=6)[:-1],
        body=fake.text(max_nb_chars=3000),
        author=choice(get_user_model().objects.all()),
    )
    a.save()
    a.categories.add(
        *sample(
            list(Category.objects.all()),
            k=4
        )
    )

for article in Article.objects.all():
    if article.comment_set.count() < 5:
        for _ in range(5):
            article.comment_set.create(
                comment=fake.sentence(nb_words=10)[:-1],
                author=choice(get_user_model().objects.all()),
            )