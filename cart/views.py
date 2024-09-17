from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.

def cart_summary(request):
    ''' get tghe cart '''
    cart = Cart(request)
    cart_products = cart.get_product

    quantities = cart.get_quantity
    totals = cart.cart_total()

    ''' returns summary about the cart '''
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})
    
def cart_add(request):
    ''' get the cart '''
    cart = Cart(request)
    ''' test for POST '''
    if request.POST.get('action') == 'post':
        ''' get stuff '''
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        ''' lookup products in database '''
        product = get_object_or_404(Product, id=product_id)
        ''' save to a session '''
        cart.add(product=product, quantity=product_qty)

        ''' get cart quantity '''
        cart_quantity = cart.__len__()

        ''' return response '''
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        messages.success(request, "Product added to the cart.")
        return response
    
    
def cart_delete(request):
    ''' delete item in cart '''
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        ''' get stuff '''
        product_id = int(request.POST.get('product_id'))
        ''' call delete function '''
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        messages.success(request, "item Removed from your cart.")
        return response

def cart_update(request):
    ''' update cart '''
    cart = Cart(request)


    if request.POST.get('action') == 'post':
        ''' get stuff '''
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        messages.success(request, f'Updated item quantity to {product_qty}.')
        return response
        #return redirect('cart_summary')
    else:
        messages.error(request, 'Invalid quantity. Please enter a positive number.')


