from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="customer_index"),
    path("vip", views.vip, name="vip_class")
]
