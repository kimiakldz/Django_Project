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
        # print(product_ids)
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            # print(product.image)
            # print(cart)

        for item in cart.values():
            item['total_price'] = round(float(item['price']) * item['quantity'], 2)
            # print(type(item['total_price']))
            yield item

    def __len__(self):
        cart_len = sum(item['quantity'] for item in self.cart.values())
        return cart_len

    def add(self, product, quantity):
        # print(quantity)
        product_id = str(product.id)
        # print(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        print(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        subtotal = sum(float(item['price']) * item['quantity'] for item in self.cart.values())
        return round(subtotal, 2)
