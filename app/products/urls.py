from django.urls import path
from products import views

urlpatterns = [
    path("<int:pk>", views.ProductDetailAPIView.as_view()),
]