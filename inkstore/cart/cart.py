from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        ''' get current session if it exists '''
        cart = self.session.get('session_key')
        
        ''' if the user is new, no session key! Create one '''
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
            
        ''' make sure cart is available on all pages '''
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        ''' logic '''
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        ''' get product ids '''
        product_ids = self.cart.keys()
        ''' lokup those keys in our products databse model '''
        products = Product.objects.filter(id__in=product_ids)
        ''' calculate totals in cart summary '''
        quantities = self.cart
        ''' satrt counting at 0 '''
        total = 0

        for key, value in quantities.items():
            ''' convert key to int so we can calculate '''
            key = int(key)
            ''' loop through products '''

            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total


    def __len__(self):
        ''' returns length of cart quantity inside cart '''
        return len(self.cart)

    def get_product(self):
        ''' get ids from the cart '''
        product_ids = self.cart.keys()
        ''' use ids to look up for product in the database '''

        products = Product.objects.filter(id__in=product_ids)
        ''' return looked up products '''

        return products

    def get_quantity(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        ''' cart update function '''
        product_id = str(product)
        product_qty = int(quantity)
        ''' get cart '''
        ourcart = self.cart
        ''' update dictionary/cart '''
        ourcart[product_id] = product_qty

        self.session.modified = True

        newcart = self.cart

        return newcart

    def delete(self, product):
        #{'1':1, '2':4}
        product_id = str(product)
        '''delete from dictionary '''

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True


