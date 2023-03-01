from rest_framework import serializers
from products.models import Product
from rest_framework.validators import UniqueValidator

def validate_title(value: str):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"'hello' is not allowed for product title")
    return value

unique_field_validator = UniqueValidator(queryset=Product.objects.all(), lookup="iexact")