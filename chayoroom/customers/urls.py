from django.urls import path
from . import views

app_names = "customer"
urlpatterns = [
    path("", views.index, name="index"),
    path("", views.vip, name="vip"),
    path("<customer_id>", views.detail, name="detail")

]
