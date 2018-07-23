from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape, escape
from datetime import datetime
from shop.models import Shop

register = template.Library()


@register.filter(name='mc')
def my_cut(value, arg=' '):
    return value.replace(arg, '')


# register.filter('my_cut', my_cut)

@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def add_italic_tags(value, autoescape=None):
    print(autoescape)
    # return f'<i>{value}</i>'
    # return conditional_escape(value)
    return escape(value)


@register.filter(expect_localtime=True)
def local_time(value):
    return value


@register.simple_tag(takes_context=True)
def current_time(context, f, prefix=None):
    prefix = prefix or context.get('date_prefix', '')
    context['t1'] = 'World'
    return prefix + datetime.now().strftime(f)


@register.simple_tag
def very_simple_tag(*args, **kwargs):
    return args, kwargs


@register.inclusion_tag('shop/test/menu.html', takes_context=True)
def menu(context, selected=None):
    return {
        'items': [
            'Menu 1',
            'Menu 2',
            'Menu 3',
        ],
        'selected': selected or context.get('selected_menu', -1),
    }


@register.simple_tag(takes_context=True)
def get_user(context):
    return context['user']


@register.simple_tag
def get_shop(pk):
    return Shop.objects.get(pk=pk)


@register.tag
def upper(parser, token):
    nodelist = parser.parse('endupper')
    parser.delete_first_token()
    return UpperNode(nodelist)


class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return self.nodelist.render(context).upper()