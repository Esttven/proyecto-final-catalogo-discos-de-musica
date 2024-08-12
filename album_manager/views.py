from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import *
from .forms import *

def index(request):
    categories = Category.objects.order_by('category_name')
    products = Product.objects.order_by('product_name')
    clients = Client.objects.order_by('name')
    purchases = Purchase.objects.order_by('total')
    template = loader.get_template('index.html')
    context = {
        'categories': categories,
        'products': products,
        'clients': clients,
        'purchases': purchases,
    }
    return HttpResponse(template.render(context, request))
#category
def category(request, category_id):
    category = Category.objects.get(id=category_id)
    template = loader.get_template('display_category.html')
    context = {
        'category': category
    }
    return HttpResponse(template.render(context, request))

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def edit_category(request, id):
    category = get_object_or_404(Category, pk = id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = CategoryForm(instance=album)
    return render(request, 'category_form.html', {'form': form})

def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('album_manager:index')
#product
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    template = loader.get_template('display_product.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def edit_product(request, id):
    product = get_object_or_404(product, pk = id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(product, pk=id)
    product.delete()
    return redirect('album_manager:index') 
#client
def album(request, album_id):
    album = Album.objects.get(id=album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})

def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

def delete_album(request, id):
    album = get_object_or_404(Album, pk=id)
    album.delete()
    return redirect('album_manager:index')
#purchase
def purchase(request, product_id):
    product = product.objects.get(id=product_id)
    template = loader.get_template('display_product.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

def add_product(request):
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = productForm()
    return render(request, 'product_form.html', {'form': form})
