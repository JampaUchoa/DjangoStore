from django.shortcuts import render

# Create your views here.
from .models import Product, Client
from .forms import ClientForm
from django.http import HttpResponseRedirect

def products(request):
    products_list = Product.objects.values()
    context = {'products': products_list}
    return render(request, 'store/products.html', context)

def client_register(request):
    # Get registering page
    if request.method == 'GET':
        client_form = ClientForm()
        return render(request, 'store/register.html', {"form": client_form})
    elif request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = Client(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'], phone=form.cleaned_data['phone'], address=form.cleaned_data['address'])
            new_client.save()
            return HttpResponseRedirect("/store")
   
'''
def add_to_cart(request, product_id):
    #
def finalize_order(request, order_id):
    #
def orders(request):
    #
'''

'''
-> Cliente cadastra-se diretamente no sistema
-> Visualizar produtos
- Adicionar Produtos no carrinho (pedido)
- Finalizar compra (fechar pedido)
- Visualizar pedidos
'''
