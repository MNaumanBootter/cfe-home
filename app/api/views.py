from django.http import HttpRequest
from products.models import Products
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
        instance: Products = serializer.save()
        print(serializer.data)
        return Response(serializer.data)