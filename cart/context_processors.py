from .cart import Cart

''' create context proccessor so cart can works
    on all pages '''
    
def cart(request):
    ''' return the default data from our cart '''
    return {'cart': Cart(request)}
