from django.shortcuts import render 

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def sale(request):
    
    return render(request, 'sale.html')

def contact(request):
    
    return render(request, 'contact.html')

def checkout(request):
    
    return render(request, 'checkout.html')

def about(request):
    
    return render(request, 'about.html')

def products(request):
    
    return render(request, 'products.html')

def single(request):
    
    return render(request, 'single.html')