from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category


# Create your views here.

class LandingView(View):
    template_name = 'home.html'

    def get(self, request, category_slug=None):
        main_categories = Category.objects.filter(is_sub=False)
        categories = Category.objects.all()
        products = Product.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            subcategories = categories.filter(parent_id=category)
            return render(request, self.template_name,
                          {'categories': subcategories, 'products': products})
        return render(request, self.template_name,
                      {'categories': main_categories, 'products': products})

    def post(self, request):
        return render(request, self.template_name)


class SubcatView(View):
    template_name = 'home.html'
    pass


class ShopView(View):
    template_name = 'shop.html'

    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})

    def post(self, request):
        return render(request, self.template_name)


class ProductDetailView(View):
    template_name = 'detail.html'

    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        return render(request, self.template_name, {'product': product})

    def post(self, request):
        return render(request, self.template_name)
