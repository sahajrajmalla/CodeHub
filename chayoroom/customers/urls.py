from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="customer_index"),
    path("", views.vip, name="customer_vip"),
    path("<customer_id>", views.detail, name="customer_detail")

]
