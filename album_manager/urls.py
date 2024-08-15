from django.urls import path
from . import views

app_name = 'album_manager'
urlpatterns = [
    path("", views.index, name="index"),
    path("genre/", views.genres, name="genres"),
    path("genre/<int:genre_id>/", views.genre, name="genre"),
    path("add_genre/", views.add_genre, name='add_genre'),
    path("edit_genre/<int:id>/", views.edit_genre, name='edit_genre'),
    path("delete_genre/<int:id>/", views.delete_genre, name='delete_genre'),
    path("disc/", views.discs, name="discs"),
    path("disc/<int:disc_id>/", views.disc, name="disc"),
    path("add_disc/", views.add_disc, name='add_disc'),
    path("edit_disc/<int:id>/", views.edit_disc, name='edit_disc'),
    path("delete_disc/<int:id>/", views.delete_disc, name='delete_disc'),
    path("client/", views.clients, name="clients"),
    path("client/<int:client_id>/", views.client, name="client"),
    path("add_client/", views.add_client, name='add_client'),
    path("edit_client/<int:id>/", views.edit_client, name='edit_client'),
    path("delete_client/<int:id>/", views.delete_client, name='delete_client'),
    path("purchase/", views.purchases, name="purchases"),
    path("purchase/<int:purchase_id>/", views.purchase, name="purchase"),
    path("add_purchase/", views.add_purchase, name='add_purchase'),
]