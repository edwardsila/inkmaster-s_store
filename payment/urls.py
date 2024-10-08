"""
URL configuration for inkstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
     path('payment_success', views.payment_success, name='payment_success'),
     path('payment_failed', views.payment_failed, name='payment_failed'),
     path('checkout', views.checkout, name='checkout'),
     path('billing_info', views.billing_info, name='billing_info'),
     path('process_order', views.process_order, name='process_order'),
     path('shipped_dash', views.shipped_dash, name='shipped_dash'),
     path('not_shipped_dash', views.not_shipped_dash, name='not_shipped_dash'),
     path('orders/<int:pk>', views.orders, name='orders'),
     path('paypal', include("paypal.standard.ipn.urls")),

]
