from django import template

register = template.Library()


# 自定义过滤器
@register.filter
def my_cut(value, arg):

    return value.replace(arg, '')


# 自定义简单的求和模板标签
@register.simple_tag
def plus(*args):

    total = 0
    for arg in args:
        total += arg
    return total
