from django import forms
from .models import *

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        widgets = {
            'genre_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DiscForm(forms.ModelForm):
    class Meta:
        model = Disc
        fields = '__all__'
        widgets = {
            'disc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'Genre_name': forms.Select(attrs={'class': 'form-control'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'Disc': forms.Select(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }