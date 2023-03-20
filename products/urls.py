from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<str:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/search/', views.ProductFilter.as_view(), name = "product-filter"),
]