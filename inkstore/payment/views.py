from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages

# Create your views here.

def process_order(request):
	''' did someone submit the form '''
	if request.POST:
		''' get billing info from last page '''
		payment_form = PaymentForm(request.POST or None)
		''' get shipping session data '''
		my_shipping = request.session.get('my_shipping')
		print(my_shipping)
		messages.success(request, "Order placed")
		return redirect('home')
	else:
		messages.success(request, "Access denied")
		return redirect('home')

def billing_info(request):
	if request.POST:
		''' get tghe cart '''
		cart = Cart(request)
		cart_products = cart.get_product

		quantities = cart.get_quantity
		totals = cart.cart_total()

		''' create session with shipping info '''
		my_shipping = request.POST
		request.session['my_shipping'] = my_shipping

		''' check to see if user is logged in '''
		if request.user.is_authenticated:
			''' get the billing form '''
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_info":request.POST, "billing_form":billing_form})
		else:
			''' not logged in '''
			''' get the billing form '''
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_info":request.POST, "billing_form":billing_form})

		shipping_form = request.POST
		return render(request, "payment/billing_info.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_form":shipping_form})
	else:
		messages.success(request, "Access denied")
		return redirect('home')

def checkout(request):

	''' get tghe cart '''
	cart = Cart(request)
	cart_products = cart.get_product

	quantities = cart.get_quantity
	totals = cart.cart_total()

	if request.user.is_authenticated:
		''' checkout as logged in user '''
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
		return render(request, "payment/checkout.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_form":shipping_form})
	else:
		''' Checkout as guest '''
		shipping_form = ShippingForm(request.POST or None)
		return render(request, "payment/checkout.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_form":shipping_form})
	

def payment_success(request):

	return render(request, "payment/payment_success.html", {})
