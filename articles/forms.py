import bleach
from bleach.css_sanitizer import CSSSanitizer
from django import forms

from .models import Article, Category


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        BODY_ALLOWED_TAGS_AND_ATTRIBUTES = {
            'h3': [], 'h4': [],
            'b': [], 'u': [], 'i': [],
            'ul': [], 'ol': [], 'li': [],
            'p': ['style'],
            'img': ['src', 'style'],
            'a': ['href', 'style'],
        }
        BODY_ALLOWED_CSS_PROPERTIES = ['color', 'width']

        model = Article
        fields = ['title', 'categories', 'body']
        help_texts = {
            'body': f'Allowed tags and their attributes: {BODY_ALLOWED_TAGS_AND_ATTRIBUTES}, '
                    f'Allowed CSS properties where applicable: {BODY_ALLOWED_CSS_PROPERTIES}'
        }

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def clean_body(self):
        return bleach.clean(
            text=self.cleaned_data['body'],
            tags=ArticleCreateForm.Meta.BODY_ALLOWED_TAGS_AND_ATTRIBUTES.keys(),
            attributes=ArticleCreateForm.Meta.BODY_ALLOWED_TAGS_AND_ATTRIBUTES,
            protocols=['https', 'http'],
            strip_comments=True,
            strip=True,
            css_sanitizer=CSSSanitizer(
                allowed_css_properties=ArticleCreateForm.Meta.BODY_ALLOWED_CSS_PROPERTIES
            ),
        )


ArticleUpdateForm = ArticleCreateForm  # create a separate form later if needed


class CategorySelectForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
