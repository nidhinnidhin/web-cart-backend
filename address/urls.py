from django.urls import path
from .views import AddressList

app_name = "address"

urlpatterns = [
    path("address/", AddressList.as_view(), name='address'),
]