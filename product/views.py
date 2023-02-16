from django.shortcuts import render
from django.views import View
from .models import Product, Category


# Create your views here.

class LandingView(View):
    def get(self, request):
        main_categories = Category.objects.filter(parent_id__category=None)
        return render(request, 'home.html', {'main_categories': main_categories})

    def post(self, request):
        return render(request, 'home.html')


class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop.html', {'products':products})

    def post(self, request):
        return render(request, 'home.html')
