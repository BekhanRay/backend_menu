from django.contrib import admin

from .models import MenuItem


@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')
    search_fields = ('title', 'url', 'parent')

