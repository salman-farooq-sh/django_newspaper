import html2text
from django import template
from furl import furl

register = template.Library()


@register.filter
def html_to_text(html):
    # TODO: configure this conversion
    return html2text.html2text(html)

