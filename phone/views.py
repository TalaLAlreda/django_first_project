from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Item, ItemDetails, Cart
from .forms import RegisterUserForm, LoginUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render({'request' : request}))

def showPhone(request):
    temp = loader.get_template('showphone.html')
    phone = ItemDetails.objects.select_related('itemId')
    print(phone.query)
    return HttpResponse(temp.render({'phone' : phone, 'request' : request}))

def details(request, id):
    temp = loader.get_template('details.html')
    phone = ItemDetails.objects.select_related('itemId').filter(id = id)

    context = {
        'phone' : phone,
        'request' : request
        
        }
    return HttpResponse(temp.render(context))

@csrf_exempt
def auth_logout(req):
    if req.method == 'POST':
        logout(req)
        return redirect('/')

@csrf_exempt
def auth_register(request):
    temp = loader.get_template('auth_register.html')
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form' : form}
    return HttpResponse(temp.render(context =context))

@csrf_exempt
def auth_login(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
    context = {'form' : form}
    return render(request, 'auth_login.html', context)

@login_required(login_url= 'login')
def checkout(request):
    temp = loader.get_template('checkout.html')
    current_user = request.user.id
    cart = Cart.objects.all().filter(id_user = current_user).first()
    product = Item.objects.all().filter(id = cart.id_product).first()
    return HttpResponse(temp.render({'request' : request, 'cart' : cart, 'product' : product}))

@login_required(login_url= 'login')
def addToCart(request, id):
    currentUser = request.user
    discount = 2
    state = False
    phone = ItemDetails.objects.select_related('itemId').filter(id = id)
    for item in phone:
        cartData = Cart(
        id_user = currentUser.id,
        id_product = item.itemId.id,
        price = item.price,
        quantity = item.quantity,
        tax = item.tax,
        total = item.total,
        discount = discount,
        net = item.total - discount,
        status = state
        )


        cartData.save()
    count = Cart.objects.filter(id_user = currentUser.id).count()
    request.session['cartCount'] = count
    return redirect('/phones/')