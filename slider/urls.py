from django.urls import path
from . import views

app_name = "slider"

urlpatterns = [
    path('', views.SliderListView.as_view(), name='slider'),
]

