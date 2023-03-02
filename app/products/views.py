from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from api.mixins import (
    StaffEditorPermissionMixin,
    UserQuerySetMixin
    )


class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)



class ProductDetailAPIView(
    UserQuerySetMixin,
    generics.RetrieveAPIView,
    StaffEditorPermissionMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(
    UserQuerySetMixin,
    generics.UpdateAPIView,
    StaffEditorPermissionMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(
    UserQuerySetMixin,
    generics.DestroyAPIView,
    StaffEditorPermissionMixin):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"

    # def perform_destroy(self, instance):
    #     return super().perform_destroy(instance)