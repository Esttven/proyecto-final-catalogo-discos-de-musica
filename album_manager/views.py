from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    discs = Disc.objects.order_by('disc_name')
    clients = Client.objects.order_by('name')
    purchases = Purchase.objects.order_by('total')
    template = loader.get_template('index.html')
    context = {
        'genres': genres,
        'discs': discs,
        'clients': clients,
        'purchases': purchases,
    }
    return HttpResponse(template.render(context, request))
#genre
def genres(request):
    genres = Genre.objects.order_by('id')
    template = loader.get_template('display_genres.html')
    context = {
        'genres': genres
    }
    return HttpResponse(template.render(context, request))

def genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    template = loader.get_template('display_genre.html')
    context = {
        'genre': genre
    }
    return HttpResponse(template.render(context, request))

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = GenreForm()
    return render(request, 'genre_form.html', {'form': form})

def edit_genre(request, id):
    genre = get_object_or_404(Genre, pk = id)
    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_form.html', {'form': form})

def delete_genre(request, id):
    genre = get_object_or_404(Genre, pk=id)
    genre.delete()
    return redirect('album_manager:index')

#disc
def disc(request, disc_id):
    disc = Disc.objects.get(id=disc_id)
    template = loader.get_template('display_disc.html')
    context = {
        'disc': disc
    }
    return HttpResponse(template.render(context, request))

def discs(request):
    template = loader.get_template('display_discs.html')
    context = {
        'disc': disc
    }
    return HttpResponse(template.render(context, request))

def add_disc(request):
    if request.method == 'POST':
        form = DiscForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = DiscForm()
    return render(request, 'disc_form.html', {'form': form})

def edit_disc(request, id):
    disc = get_object_or_404(Disc, pk = id)
    if request.method == 'POST':
        form = DiscForm(request.POST, request.FILES, instance=disc)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = DiscForm(instance=disc)
    return render(request, 'disc_form.html', {'form': form})

def delete_disc(request, id):
    disc = get_object_or_404(Disc, pk=id)
    disc.delete()
    return redirect('album_manager:index') 

#client
def clients(request):
    clients = Client.objects.order_by('id')
    template = loader.get_template('display_clients.html')
    context = {
        'clients': clients
    }
    return HttpResponse(template.render(context, request))
@login_required
def client(request, client_id):
    client = Client.objects.get(id=client_id)
    template = loader.get_template('display_client.html')
    context = {
        'client': client
    }
    return HttpResponse(template.render(context, request))

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def edit_client(request, id):
    client = get_object_or_404(Client, pk = id)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return redirect('album_manager:index')

#purchase
def purchases(request):
    purchases = Purchase.objects.order_by('total')
    template = loader.get_template('display_purchases.html')
    context = {
        'pruchases': purchases
    }
    return HttpResponse(template.render(context, request))
@login_required
def purchase(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    template = loader.get_template('display_purchase.html')
    context = {
        'purchase': purchase
    }
    return HttpResponse(template.render(context, request))

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = PurchaseForm()
    return render(request, 'purchase_form.html', {'form': form})
