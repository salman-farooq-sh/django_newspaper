from django import forms

from .models import Article, Category


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'categories', 'body']

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


ArticleUpdateForm = ArticleCreateForm  # create a separate form later if needed


class CategorySelectForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
