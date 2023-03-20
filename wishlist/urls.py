from django.urls import path
from . import views

app_name = "wishlist"

urlpatterns = [
    path("", views.WishlistView.as_view(), name="wishlist"),
    path("wishlistlisting/", views.WishlistListing.as_view(), name="wishlistlisting"),
    path('<str:pk>/', views.WishlistDetail.as_view(), name="wishlistdetail"),
    path('wishlistdelete/<str:pk>/', views.WishlistDelete.as_view(), name="wishlistdelete")
]
