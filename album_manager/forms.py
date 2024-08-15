from django import forms
from .models import *

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        labels = {
            "genre_name":  "Nombre",
        }
        widgets = {
            'genre_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DiscForm(forms.ModelForm):
    class Meta:
        model = Disc
        fields = '__all__'
        labels = {
            "disc_name":  "Nombre",
            "price": "Precio",
            "artist": "Artista",
            "genre": "Género",
            "cover": "Portada",
        }
        widgets = {
            'disc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'cover': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            "name":  "Nombre",
            "country": "País",
            "age": "Edad",
            "email": "Correo electrónico",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'nombre@ejemplo.com'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('client', 'discs', 'purchase_date')
        labels = {
            "client": "Cliente",
            "discs": "Ítems",
            "purchase_date": "Fecha",
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-select'}),
            'discs': forms.CheckboxSelectMultiple(),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }