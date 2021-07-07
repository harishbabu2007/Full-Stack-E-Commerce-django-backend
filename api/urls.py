from django.urls import path
from . import views

urlpatterns = [
    path("react/check_is_auth", views.check_is_auth),
    path("react/list_products", views.list_products),
    path("react/get_product_by_slug", views.get_product_by_slug),
    path("react/get_products_by_category", views.get_products_by_category),
    path("react/add_product_cart", views.add_product_cart),
    path("react/get_cart_products", views.get_cart_products),
    path("react/delete_item_cart", views.delete_item_cart),
    path("react/get_cart_price", views.get_cart_price), 
    path("react/purchase_items", views.purchase_items),
    path("react/search_products", views.search_products),
]