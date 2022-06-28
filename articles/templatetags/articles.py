# from django import template
# from furl import furl
#
# register = template.Library()
#
#
# @register.filter
# def add_get_parameter(url, parameter):
#     parameter_name, parameter_value = parameter.split('=', maxsplit=2)
#     f = furl(url)
#     f.args[parameter_name] = parameter_value
#     return f.url
#
