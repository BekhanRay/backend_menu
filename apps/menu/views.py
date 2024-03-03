
from django.shortcuts import render
from .models import MenuItem


def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name)
    return render(request, 'menu.html', {'menu_items': menu_items})
