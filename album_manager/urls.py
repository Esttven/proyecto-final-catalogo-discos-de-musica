from django.urls import path
from . import views

app_name = 'album_manager'
urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id>/", views.category, name="category"),
    path("add_category/", views.add_category, name='add_category'),
    path("edit_category/<int:id>/", views.edit_category, name='edit_category'),
    path("delete_category/<int:id>/", views.delete_category, name='delete_category'),
    path("product/<int:product_id>/", views.product, name="product"),
    path("add_product/", views.add_product, name='add_product'),
    path("edit_product/<int:id>/", views.edit_product, name='edit_product'),
    path("delete_product/<int:id>/", views.delete_product, name='delete_product'),
    path("client/<int:client_id>/", views.client, name="client"),
    path("add_client/", views.add_client, name='add_client'),
    path("edit_client/<int:id>/", views.edit_client, name='edit_client'),
    path("delete_client/<int:id>/", views.delete_client, name='delete_client'),
    path("purchase/<int:purchase_id>/", views.purchase, name="purchase"),
    path("add_purchase/", views.add_purchase, name='add_purchase'),
    path("edit_purchase/<int:id>/", views.edit_purchase, name='edit_purchase'),
    path("delete_purchase/<int:id>/", views.delete_purchase, name='delete_purchase'),
]