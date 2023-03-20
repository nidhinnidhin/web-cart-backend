from django.urls import path
from .views import Register,AccountEditView, BlacklistTokenUpdateView, ForgetPasswordGenerateOTP, ResetPassword, AccountDetail
from django.contrib.auth import views as auth_views


app_name = "account"

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("accountedit/", AccountEditView.as_view(), name="accountedit"),
    path("accountdetail/", AccountDetail.as_view(), name="accountdetail"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('generate-otp/', ForgetPasswordGenerateOTP.as_view(), name = "generate-otp"),
    path('reset-password/', ResetPassword.as_view(), name = "reset-password"),
]