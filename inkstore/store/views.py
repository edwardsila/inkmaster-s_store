from django.shortcuts import render

'''Create your views here.'''

def home(request):
    ''' view for our home page '''
    return render(request, 'home.html', {})
