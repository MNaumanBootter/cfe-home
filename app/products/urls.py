from django.urls import path
from products import views

urlpatterns = [
    path("", views.ProductMixinView.as_view()),
    path("<int:pk>", views.ProductDetailAPIView.as_view()),
    path("<int:pk>/update", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete", views.ProductDestroyAPIView.as_view()),
]