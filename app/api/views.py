from django.http import HttpRequest
from products.models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request: HttpRequest) -> Response:
    """
    DRF API View
    """
    instance = Products.objects.all().order_by("?").first()
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)