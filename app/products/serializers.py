from rest_framework import serializers

from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    class Meta:
        model = Products
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Products):
            return None
        return obj.get_discount()
