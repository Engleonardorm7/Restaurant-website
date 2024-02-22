from .models import MenuItem
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm

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
    form = BookingForm()
    success_message = None 
    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Reservation made successfully!"
    return render(request,'book.html', {'form': form, 'success_message': success_message})