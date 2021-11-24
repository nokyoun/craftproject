import json
from django.contrib.auth import authenticate, forms, login, logout
from django.http import HttpResponse, request
from django.shortcuts import redirect, render

from templates.decorator import admin_only, unauthenticated_user
from django.contrib.auth.models import Group

#import authentication
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def registerPage(request):
    print("sign up")
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            print(group)
            
            print('saved')
            messages.success(request,'Account was created for '+ username)
            return redirect('signup')
        else:
            print('not save')
    context = {'form':form}
    return render(request, 'authentication/signup.html', context)


def signup(request):
    print("log in")
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('login success')
            return redirect('home')
        else:
           print('incorrect')
           messages.info(request,'Username or password is incorrect')
                        
    context = {}
    return render(request, 'authentication/signin.html', context)



def logoutUser(request):
    logout(request)
    print('logout')
    return redirect('home')


def store(request):
    #wake
    products = Product.objects.filter(brand_id=2)
    context = {'products':products}
    return render(request, 'store/store.html', context)

def store2(request):
    #jew4u
    products = Product.objects.filter(brand_id=1)
    context = {'products':products}
    return render(request, 'store/store2.html', context)

def store3(request):
    #bhunyawat
    products = Product.objects.filter(brand_id=4)
    context = {'products':products}
    return render(request, 'store/store3.html', context)

def home(request):
    last_ten = Product.objects.filter()[:9]
    last_ten_in_ascending_order = reversed(last_ten)
    context = {'products':last_ten_in_ascending_order}
    return render(request, 'store/home.html', context)

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')


def updateItem(request):
    pData = json.loads(request.body)
    productId = pData['productId']
    action = pData['action']

    print('action:', action)
    print('productID:', productId)  
        
    return JsonResponse('item:',safe=False)


@admin_only
def manage(request):
     return render(request, 'store/managePage.html')


def custPage(request):
    return render(request, 'store/custPage.html')

def viewBtn(request):
    print('viewbtn')
    context = {}
    return render(request,'store/viewPage.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderite_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
    context = {'items':items, 'order':order}
    return render(request,'store/custPage.html', context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html')
 