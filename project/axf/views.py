from django.shortcuts import render
from .models import *
# Create your views here.


def home_views(request):
    title = '主页'
    wheelsList = Wheel.objects.all()
    return render(request,'axf/home.html',locals())

def market_views(request):
    title = '闪送超市'
    return render(request,'axf/market.html',locals())

def cart_views(request):
    title = '购物车'
    return render(request,'axf/cart.html',locals())

def mine_views(request):
    title = '我的'
    return render(request,'axf/mine.html',locals())


