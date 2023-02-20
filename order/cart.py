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
        print(product_ids)
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product.name
            cart[str(product.id)]['image'] = product.image
            print(product.image)
            print(cart)

        for item in cart.values():
            item['total_price'] = float(item['price']) * item['quantity']
            print(type(item['total_price']))
            yield item

    def add(self, product, quantity):
        print(quantity)
        product_id = str(product.id)
        print(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True


