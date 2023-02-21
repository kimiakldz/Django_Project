from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CartAddForm
from .cart import Cart
from product.models import Product


# Create your views here.


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        # print(cart)
        return render(request, 'cart.html', {'cart': cart})


class CartAddView(PermissionRequiredMixin, View):
    form_class = CartAddForm
    permission_required = 'orders.add_order'

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
