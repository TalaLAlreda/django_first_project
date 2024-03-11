from django.shortcuts import render
from phone.models import Item, ItemDetails
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def getItems(req):
    phones = Item.objects.all() # Get all Items which are phones
    phonesList = list(phones.values())
    return JsonResponse({
            'phone' : phonesList
        })

@api_view(['GET'])
def getItemsDetails(req):
    phones = ItemDetails.objects.select_related('itemId').all()
    phonesList = list(phones.values())
    list1 = []
    for item in phones:
        getItems = {
            'id' : item.id,
            'name' : item.itemId.name,
            'color' : item.color,
            'price' : item.price,
            'quantity' : item.quantity,
            'tax' : item.tax,
            'total' : item.total,
        }
        list1.append(getItems)
    return JsonResponse({
        'phone' : list1
    })

@api_view(['GET'])
def getItemsDetailsByID(req, id):
    phones = ItemDetails.objects.select_related('itemId').all().filter(id = id)
    phonesList = list(phones.values())
    list1 = []
    for item in phones:
        getItems = {
            'id' : item.id,
            'name' : item.itemId.name,
            'color' : item.color,
            'price' : item.price,
            'quantity' : item.quantity,
            'tax' : item.tax,
            'total' : item.total,
        }
        list1.append(getItems)
    return JsonResponse({
        'phone' : list1
    })