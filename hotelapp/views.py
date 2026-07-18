from django.shortcuts import render
from .models import Menu

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def menu(request):
    menus = Menu.objects.all()
    return render(request, "menu.html", {"menus": menus})

def order(request):
    return render(request, "order.html")