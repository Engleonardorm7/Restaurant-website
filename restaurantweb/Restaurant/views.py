from django.shortcuts import render
from .models import MenuItem
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home_view(request):
    return render(request,'home.html')


def menu_view(request):
    menu_items=MenuItem.objects.all().order_by('name')
    context={'menu_items': menu_items}
    return render(request,'menu.html', context)

def menu_detail(request,pk):
    item=get_object_or_404(MenuItem, pk=pk)
    context={'item':item}
    return render(request, 'menu_detail.html', context)
    
def about_view(request):
    return render(request,'about.html')

def book_view(request):
    return render(request,'book.html')