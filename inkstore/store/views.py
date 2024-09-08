from django.shortcuts import render
from .models import Product

'''Create your views here.'''


def home(request):
    ''' view for our home page '''
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
    
def about(request):
    ''' view for our home page '''
    return render(request, 'about.html', {})
