from django import template
from apps.menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name)
    return {'menu_items': menu_items}

