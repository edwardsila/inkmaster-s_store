from django.shortcuts import render, redirect
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
    ''' did they fill out the login form?? '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request, ("Please check your username and password!"))
            return redirect('login')
    
    else:    
        return render(request, 'login.html', {})
    
def logout_user(request):
    ''' view for user logout '''
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home')
