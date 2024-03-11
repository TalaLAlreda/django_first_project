"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from phone import views as vshop
from homeAppliance import views as vHome
from phone_api import views as vApi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vshop.index, name = 'index'),
    path('login/', vshop.auth_login, name='login'),
    path('register/', vshop.auth_register, name='register'),
    path('phones/', vshop.showPhone, name = 'showPhone'),
    path('phones/details/<int:id>', vshop.details, name='showDetails'),
    path('logout/', vshop.auth_logout, name = 'logout'),
    path('phones/checkout/', vshop.checkout, name = 'checkout'),
    path('add_to_cart/<int:id>/', vshop.addToCart, name = 'addToCart'),
    path('api/itemList/all', vApi.getItems, name = 'getItems'),
    path('api/itemList/all/detailed', vApi.getItemsDetails, name = 'getItemDetails'),
    path('api/itemList/all/detailed/<int:id>', vApi.getItemsDetailsByID, name = 'getItemDetailsByID'),
    path('homeAppliances/', vHome.showAppliance, name = 'showApppliance'),
    path('homeAppliances/details/<int:id>', vHome.showDetails, name ='details'),
    path('homeAppliances/details/addToCart/<int:id>', vHome.addToCart, name='addToCartH'),
    path('homeAppliances/cart/', vHome.showCart, name = 'showCart'),
    path('homeAppliances/buyNow/', vHome.buyNow, name ='buyNow')
]
