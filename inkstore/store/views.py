from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django.db.models import Q
import json
from cart.cart import Cart


'''Create your views here.'''


def search(request):
    ''' check if the filled out the form '''
    if request.method == "POST":
        searched = request.POST['searched']
        ''' Query the products '''
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        ''' test for null '''
        if not searched:
            messages.success(request, "That product does not exist!!")
            return render(request, "search.html", {})
        else:
            return render(request, "search.html", {'searched':searched})
    else:
        return render(request, "search.html", {})



def update_info(request):
    if request.user.is_authenticated:
        ''' need to know which user '''
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()

            messages.success(request, "Your info has been updated!!")
            return redirect('home')

        return render(request, "update_info.html", {'form':form})

    else:
        messages.success(request, "You must be logged in to access that page!!")
        return redirect('home')


def category_summary(request):
    ''' get all the cattegories '''
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {'categories': categories})

    


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        ''' did the fill out the page? '''
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            ''' is form valid '''
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been Updated....")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')




def update_user(request):
    if request.user.is_authenticated:
        ''' need to know which user '''
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "User has been updated!!")
            return redirect('home')

        return render(request, "update_user.html", {'user_form':user_form})

    else:
        messages.success(request, "You must be logged in to access that page")
        return redirect('home')


def category_summary(request):
    ''' get all the cattegories '''
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {'categories': categories})


def category(request, foo):
    ''' view for the category page '''
    ''' replace hiphens with space '''
    foo = foo.replace('-', ' ')
    ''' grab the cattegory from the url '''
    try:
        ''' look up the cattegory '''
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    
    except:
        messages.success(request, ("That cattegory doesnt exist!!"))
        return redirect('home')


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

            ''' some shopping cart '''
            current_user = Profile.objects.get(user__id=request.user.id)
            ''' get their saved cart from the database '''
            saved_cart = current_user.old_cart
            '''convert dataase string to python dictionary '''
            if saved_cart:
                ''' convert to dictionary using json '''
                converted_cart = json.loads(saved_cart)
                ''' add the loaded cart dict to our session '''
                cart = Cart(request)
                ''' loop through the cart and add items from our dictionary '''
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

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
            messages.success(request, ("Username created please fill out your User ufo below..."))
            return redirect('update_info')
        else:
            messages.success(request, ("oops! please check your details"))
            return redirect('register')
    else:        
        return render(request, 'register.html', {'form':form})
