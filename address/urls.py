from django.urls import path
from .views import AddressList, AddressEditView, AddressDetailView

app_name = "address"

urlpatterns = [
    path("address/", AddressList.as_view(), name='address'),
    path("addressedit/", AddressEditView.as_view(), name="addressedit"),
    path("addressdetail/", AddressDetailView.as_view(), name="addressdetail"),
]