from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from accounts.models import Address
from .forms import CartAddForm, DiscountCodeForm
from .cart import Cart
from product.models import Product
from .models import Order, OrderDetail, DiscountCode
import datetime


# Create your views here.


class CartView(View):

    def get(self, request):
        cart = Cart(request)
        # print(cart)
        return render(request, 'cart.html', {'cart': cart})


class CartAddView(View):
    form_class = CartAddForm

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('order:cart')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('order:cart')


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderDetail.objects.create(order=order, product=item['product'], price=item['price'],
                                       quantity=item['quantity'])
            return redirect('order:Order_detail', order.id)


class OrderDetailView(LoginRequiredMixin, View):
    form_class = DiscountCodeForm

    def get(self, request, order_id, user_id):
        order = get_object_or_404(Order, id=order_id)
        addresses = Address.objects.filter(user_id=user_id)
        return render(request, 'checkout.html', {'order': order, 'form': self.form_class, 'addresses':addresses})


class CodeApplyView(LoginRequiredMixin, View):
    form_class = DiscountCodeForm

    def post(self, request, order_id):
        now = datetime.datetime.now()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                discount = DiscountCode.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now,
                                                    is_active=True)
            except DiscountCode.DoesNotExist:
                messages.error(request, 'This code is not valid!', 'danger')
                return redirect('order:Order_detail', order_id)
            order = Order.objects.get(id=order_id)
            order.discount_code = discount
            order.save()
        return redirect('order:Order_detail', order_id)


class PlaceOrderView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        cart = Cart(request)
        order = get_object_or_404(Order, id=order_id)
        order.is_paid = True
        cart.clear()
        return redirect('landing:landing')
