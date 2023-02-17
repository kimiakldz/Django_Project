from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category
from order.forms import CartAddForm


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


class ProductDetailView(View):
    template_name = 'detail.html'
    form_class = CartAddForm

    def get(self, request, product_slug):
        form = self.form_class
        product = get_object_or_404(Product, slug=product_slug)
        return render(request, self.template_name, {'product': product, 'form': form})

    def post(self, request):
        return render(request, self.template_name)
