from django.forms.models import model_to_dict
from django.http import HttpRequest
from products.models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request: HttpRequest) -> Response:
    """
    DRF API View
    """
    model_data = Products.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "content", "price"])
    return Response(data)