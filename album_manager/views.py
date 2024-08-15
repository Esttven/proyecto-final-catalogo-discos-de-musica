from django.http import HttpResponse
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
#genre
def genres(request):
    genres = Genre.objects.order_by('genre_name')
    template = loader.get_template('display_genres.html')
    context = {
        'genres': genres,
        'messages': messages.get_messages(request),
    }
    return HttpResponse(template.render(context, request))

def genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    discs = Disc.objects.filter(genre=genre)
    template = loader.get_template('display_genre.html')
    context = {
        'genre': genre,
        'discs': discs
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_manager:genres')
    else:
        form = GenreForm()
    return render(request, 'genre_form.html', {'form': form})

@login_required
def edit_genre(request, id):
    genre = get_object_or_404(Genre, pk = id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('album_manager:genres')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_form.html', {'form': form})

@login_required
def delete_genre(request, id):
    if request.method == 'POST':
        try:
            genre = get_object_or_404(Genre, pk=id)
            genre.delete()
        except ProtectedError:
            messages.error(request, "No se puede eliminar este género porque contiene discos dentro.")
    
    return redirect('album_manager:genres')
    
#disc
def disc(request, disc_id):
    disc = Disc.objects.get(id=disc_id)
    template = loader.get_template('display_disc.html')
    context = {
        'disc': disc
    }
    return HttpResponse(template.render(context, request))

def discs(request):
    discs = Disc.objects.order_by('artist')
    template = loader.get_template('display_discs.html')
    context = {
        'discs': discs
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_disc(request):
    if request.method == 'POST':
        form = DiscForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:discs')
    else:
        form = DiscForm()
    return render(request, 'disc_form.html', {'form': form})

@login_required
def edit_disc(request, id):
    disc = get_object_or_404(Disc, pk = id)
    if request.method == 'POST':
        form = DiscForm(request.POST, request.FILES, instance=disc)
        if form.is_valid():
            form.save()
            return redirect('album_manager:discs')
    else:
        form = DiscForm(instance=disc)
    return render(request, 'disc_form.html', {'form': form})

@login_required
def delete_disc(request, id):
    disc = get_object_or_404(Disc, pk=id)
    disc.delete()
    return redirect('album_manager:discs')

#client
def clients(request):
    clients = Client.objects.order_by('id')
    template = loader.get_template('display_clients.html')
    context = {
        'clients': clients
    }
    return HttpResponse(template.render(context, request))

def client(request, client_id):
    client = Client.objects.get(id=client_id)
    template = loader.get_template('display_client.html')
    context = {
        'client': client
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_manager:clients')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

@login_required
def edit_client(request, id):
    client = get_object_or_404(Client, pk = id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('album_manager:clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

@login_required
def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return redirect('album_manager:clients')

#purchase
def purchases(request):
    purchases = Purchase.objects.order_by('id')
    template = loader.get_template('display_purchases.html')
    context = {
        'purchases': purchases
    }
    return HttpResponse(template.render(context, request))

def purchase(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    template = loader.get_template('display_purchase.html')
    context = {
        'purchase': purchase
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_purchase(request):
    discs = Disc.objects.order_by('artist')
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.save()
            discs = form.cleaned_data['discs']
            purchase.discs.set(discs)
            purchase.total = sum(disc.price for disc in purchase.discs.all())
            purchase.save()
            return redirect('album_manager:purchases')
    else:
        form = PurchaseForm()

    return render(request, 'purchase_form.html', {'form': form, 'discs': discs})

class CustomLoginView(LoginView):
    template_name = 'login.html'
