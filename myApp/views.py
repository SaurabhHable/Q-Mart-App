from django.shortcuts import render, redirect
from .forms import productRegistration
from .models import Product, Category

# Create your views here.
def home(request):
    if request.method == "POST":
        form = productRegistration(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list')
    form = productRegistration()
    return render(request,'myApp/home.html', {'form':form})

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