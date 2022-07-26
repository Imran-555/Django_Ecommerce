from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from Ecommerce_app.models.coustmer import Customer
from django.views import View

from Ecommerce_app.models.product import Product
from Ecommerce_app.models.orders import Order
from Ecommerce_app.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})