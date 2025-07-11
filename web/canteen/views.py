from django.shortcuts import render, get_object_or_404
from .models import Menu


def menu_list(request):
    ob_menus = Menu.objects.all()
    return render(request, 'menu_list.html', {'menus': ob_menus})

def menu_detail(request, pk):
    ob_menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_detail.html', {'menu': ob_menu})
