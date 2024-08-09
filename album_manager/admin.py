from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass