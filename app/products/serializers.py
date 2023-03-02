from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from products.validators import unique_field_validator, validate_title

class ProductSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="pk")
    title = serializers.CharField(validators=[unique_field_validator, validate_title])

    class Meta:
        model = Product
        fields = [
            "id",
            "user_id",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
            "url",
            "edit_url",
        ]

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
