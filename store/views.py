import datetime
from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import ClientForm
from django.http import HttpResponseRedirect

def products(request):
    """ Return a product list """
    products_list = Product.objects.values()
    cart = Order.objects.last().products.values_list('id', flat=True)

    context = {'products': products_list, 'cart': cart}
    return render(request, 'store/products.html', context)

def client_register(request):
    """ Client registration portal """
    # Get registering page
    if request.method == 'GET':
        client_form = ClientForm()
        return render(request, 'store/register.html', {"form": client_form})
    elif request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = Client(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'], phone=form.cleaned_data['phone'], 
                                address=form.cleaned_data['address'])
            new_client.save()
            return HttpResponseRedirect("/")

def orders(request):
    """ Client orders index """
    order_list = Order.objects.all().prefetch_related('products')
    context = {'orders': order_list}
    return render(request, 'store/orders.html', context)

def toggle_cart(request, product_id):
    """ Toggles a product form the shopping list """
    order = Order.objects.last()
    if order.status == "Closed":
        order = Order(status="Open", created_at=datetime.datetime.now(), 
                      client_id=Client.objects.last().id)
        order.save()
    added = order.products.all().filter(id=product_id)
    if not added:
        order.products.add(Product.objects.get(id=product_id))
    else:
        order.products.remove(Product.objects.get(id=product_id))
    return HttpResponseRedirect("/")

def checkout(request):
    """ Shows all the orders so far """
    order = Order.objects.last()

    if request.method == 'GET':
        context = {'order': order}
        return render(request, 'store/checkout.html', context)
    elif request.method == 'POST':
        order.status = "Closed"
        order.created_at = datetime.datetime.now()
        order.save()
    return HttpResponseRedirect("/orders")
