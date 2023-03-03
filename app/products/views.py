from rest_framework import generics
from products.models import Product, ProductQuerySet
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


class ProductSearchView(
    generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs: ProductQuerySet = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results