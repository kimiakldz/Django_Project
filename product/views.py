from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from order.forms import CartAddForm

from product.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
        print(cart)

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product.name

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True


# Create your views here.

class LandingView(View):
    template_name = 'home.html'

    def get(self, request):
        main_categories = Category.objects.filter(is_sub=False)
        categories = Category.objects.all()
        products = Product.objects.all()
        return render(request, self.template_name,
                      {'categories': main_categories, 'products': products})

    def post(self, request):
        return render(request, self.template_name)


class ShopView(View):
    template_name = 'shop.html'

    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.all()
        main_categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            subcategories = categories.filter(parent_id=category)
            products = products.filter(category_id=category)
            return render(request, self.template_name,
                          {'categories': subcategories, 'products': products, 'mcat': main_categories})
        return render(request, self.template_name, {'products': products, 'mcat': main_categories})

    def post(self, request):
        return render(request, self.template_name)

# class NavView(View):
#     template_name = 'inc/navbar.html'
#
#     def get(self, request):
#         products = Product.objects.all()
#         categories = Category.objects.all()
#         main_categories = Category.objects.filter(is_sub=False)
#         return render(request, self.template_name, {'products': products, 'mcat': main_categories})
#
#     def post(self, request):
#         return render(request, self.template_name)

class ProductDetailView(View):
    template_name = 'detail.html'
    form_class = CartAddForm

    def get(self, request, product_slug):
        form = self.form_class
        product = get_object_or_404(Product, slug=product_slug)
        return render(request, self.template_name, {'product': product, 'form': form})

    def post(self, request):
        return render(request, self.template_name)
