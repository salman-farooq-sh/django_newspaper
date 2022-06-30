# import html2text
from bs4 import BeautifulSoup
from django import template

register = template.Library()


@register.filter
def html_to_text(html):
    # text_maker = html2text.HTML2Text()
    #
    # text_maker.ignore_links = True
    # text_maker.skip_internal_links = True
    # text_maker.ignore_anchors = True
    # text_maker.ignore_emphasis = True
    # text_maker.ignore_tables = True
    # text_maker.ignore_images = True
    # text_maker.single_line_break = True
    # text_maker.emphasis = False
    # text_maker.strong_mark = ''
    # text_maker.emphasis_mark = ''
    #
    # return text_maker.handle(html)

    return ' '.join(BeautifulSoup(html, "html.parser").stripped_strings)
