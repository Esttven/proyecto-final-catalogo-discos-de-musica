from django.urls import path
from . import views

app_name = 'album_manager'
urlpatterns = [
    path("", views.index, name="index"),
    path("genre/", views.genres, name="genres"),
    path("genre/<int:genre_id>/", views.genre, name="genre"),
    path("genre/add/", views.add_genre, name='add_genre'),
    path("genre/edit/<int:id>/", views.edit_genre, name='edit_genre'),
    path("genre/delete/<int:id>/", views.delete_genre, name='delete_genre'),
    path("disc/", views.discs, name="discs"),
    path("disc/<int:disc_id>/", views.disc, name="disc"),
    path("disc/add/", views.add_disc, name='add_disc'),
    path("disc/edit/<int:id>/", views.edit_disc, name='edit_disc'),
    path("disc/delete/<int:id>/", views.delete_disc, name='delete_disc'),
    path("client/", views.clients, name="clients"),
    path("client/<int:client_id>/", views.client, name="client"),
    path("client/add/", views.add_client, name='add_client'),
    path("client/edit/<int:id>/", views.edit_client, name='edit_client'),
    path("client/delete/<int:id>/", views.delete_client, name='delete_client'),
    path("purchase/", views.purchases, name="purchases"),
    path("purchase/<int:purchase_id>/", views.purchase, name="purchase"),
    path("purchase/add/", views.add_purchase, name='add_purchase'),
    path("login/", views.CustomLoginView.as_view(), name='login'),
]