from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.CartList.as_view(), name = "cart-list"),
    path("cart-product/", views.CartListItems.as_view(), name="cart-product"),
    path("cart-product-decrement/", views.CartDecrement.as_view(), name="cart-product-decrement"),
    path("<int:pk>/", views.CartDetail.as_view(), name="cart-detail"),
    path("cartDelete/<int:pk>/", views.CartDelete.as_view(), name="cart-delete"),
]