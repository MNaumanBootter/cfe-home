from django.urls import path
from products import views

urlpatterns = [
    path("", views.product_alt_view),
    path("<int:pk>", views.product_alt_view),
]