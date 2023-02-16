from django.shortcuts import render
from django.views import View
from .models import Product, Category


# Create your views here.

class LandingView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'home.html', {'categories': categories})

    def post(self, request):
        return render(request, 'home.html')
