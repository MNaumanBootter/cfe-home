from django.http import HttpRequest
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request: HttpRequest) -> Response:
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance: Product = serializer.save()
        print(serializer.data)
        return Response(serializer.data)