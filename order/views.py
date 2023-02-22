from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CartAddForm
from .cart import Cart
from product.models import Product
from .models import Order, OrderDetail, DiscountCode


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
        print(product)
        print(type(product))
        cart.remove(product)
        return redirect('order:cart')


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user_id=request.user)
        for item in cart:
            OrderDetail.objects.create(order_id=order, product_id=item['product'], price=item['price'],
                                       quantity=item['quantity'])
            cart.clear()
            return redirect('order:Order_detail', order.id)


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        print(order)
        return render(request, 'checkout.html', {'order': order})
