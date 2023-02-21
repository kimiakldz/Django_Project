from order.cart import Cart
from .models import Category


def cart(request):
    return {'cart': Cart(request)}


def menu(request):
    categories = Category.objects.all()
    main_categories = Category.objects.filter(is_sub=False)
    return {'categories': categories, 'mcat': main_categories}

