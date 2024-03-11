from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, Cart, CartProducts
from django.contrib.auth.decorators import login_required
# Create your views here.

def showAppliance(request):
    temp = loader.get_template('appliance.html')
    product = Product.objects.all()
    return HttpResponse(temp.render({'request' : request, 'product' : product}))

def showDetails(request, id):
    temp = loader.get_template('applianceDetail.html')
    product = Product.objects.filter(id = id).first()
    return HttpResponse(temp.render({'request' : request, 'product' : product}))

@login_required(login_url= 'login')
def addToCart(request, id):
    temp = loader.get_template('appliance.html')
    currentUser = request.user
    cart = Cart.objects.filter(user_id = currentUser.id, payed = 0).first()
    if(cart == None):
        product = Product.objects.filter(id = id).first()
        cartObject = Cart(
            user_id = currentUser,
            total = product.price + product.shipment_fee,
            payed = 0
        )
        cartObject.save()
        cart = Cart.objects.filter(user_id = currentUser.id, payed = 0).first().id
        cartProductObject = CartProducts(
            cart_id = cart,
            product_id = product
        )
        cartProductObject.save()
    else:
        product = Product.objects.filter(id = id).first()
        cartObject = Cart(
            id = cart.id,
            user_id = cart.user_id,
            total = product.price + product.shipment_fee + cart.total,
            payed = 0
        )
        cartObject.save()
        cart = Cart.objects.filter(user_id = currentUser.id, payed = 0).first()
        cartProductObject = CartProducts(
            cart_id = cart,
            product_id = product
        )
        cartObject.save()
        cartProductObject.save()
    return redirect('/', request = request)

@login_required(login_url= 'login')
def showCart(request):
    temp = loader.get_template('cart.html')
    currentUser = request.user
    cart = Cart.objects.filter(user_id = currentUser.id, payed = 0).first()
    cartId = cart.id
    price = cart.total
    cartItems = CartProducts.objects.filter(cart_id = cartId).select_related('product_id')
    total = cartItems.count()
    print(cartItems, total, price)
    return HttpResponse(temp.render({'request' : request, 'cartItems' : cartItems, 'total' : total, 'price' : price}))

@login_required(login_url = 'login')
def buyNow(request):
    currentUser = request.user.id
    cart = Cart.objects.filter(user_id = currentUser, payed = 0).first()
    cartObject = Cart(
        id = cart.id,
        user_id = cart.user_id,
        total = cart.total,
        payed = 1
    )

    cartObject.save()
    return redirect('/homeAppliances')
