from django.shortcuts import render, redirect
from .forms import productRegistration
from .models import Product, Category
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests
import json

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = productRegistration(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/list')
        else:
            form = productRegistration()
    else:
        messages.info(request, 'You need to Sign up/Login first in order to add your products.')
    return render(request,'myApp/home.html', {'form':form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            #Recaptcha
            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LdvJ_AjAAAAAIxy_msVyLpGRMlIKDGVF7MsB35e'
            captchaData = {
                'secret':secretKey,
                'response':clientKey
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)
            verify = response['success']
    
            user = authenticate(request, username=username, password=password)
            if (user is not None) and (verify):
                login(request, user)
                return redirect('list')
            elif (user is not None) and (not verify):
                messages.info(request, 'Please fill the Recaptcha.')
            else:
                messages.info(request, 'Username or Password is incorrect.')
        context = {}
        return render(request,'myApp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('list')

# @login_required(login_url='login')
def list(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'myApp/list.html', data)

def productDetails(request, id):
    product=Product.objects.filter(id = id).first()
    context={
        'product':product
    }
    return render(request, 'myApp/productDetail.html', context)

def updateProd(request, id):
    product=Product.objects.get(id = id)
    form = productRegistration(instance=product)
    if request.method == 'POST':
        form = productRegistration(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list')
    context={
        'product':product,
        'form':form
    }
    return render(request, 'myApp/update_prod.html', context)