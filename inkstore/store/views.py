from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

'''Create your views here.'''


def product(request, pk):
    ''' view for the products themselves '''
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

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
    
def register_user(request):
    ''' view to register user '''
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            ''' login user '''
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered succesfully!"))
            return redirect('home')
        else:
            messages.success(request, ("oops! please check your details"))
            return redirect('register')
    else:        
        return render(request, 'register.html', {'form':form})
