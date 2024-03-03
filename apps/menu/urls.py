from django.urls import path
from .views import *

urlpatterns = [
    path('draw_menu/<str:menu_name>/', draw_menu, name='draw_menu'),
]
