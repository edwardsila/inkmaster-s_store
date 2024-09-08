from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


'''Create your views here.'''


def home(request):
    ''' view for our home page '''
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
    
def about(request):
    ''' view for our home page '''
    return render(request, 'about.html', {})
    
def login_user(request):
    ''' view for user login '''
    return render(request, 'login.html', {})
    
def logout_user(request):
    pass
