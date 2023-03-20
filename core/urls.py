from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/account/', include('account.urls', namespace ="account")),
    path('api/product/', include('products.urls', namespace ="products")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('slider/',include('slider.urls', namespace="slider")),
    path('announcement/',include('announcement.urls', namespace="announcement")),
    path('address/',include('address.urls', namespace="address")),
    path('checkout/', include('checkout.urls', namespace="checkout")),
    path('wishlist/', include('wishlist.urls', namespace="wishlist")),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)