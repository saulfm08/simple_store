from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from product.client import ProductClient


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def products(request):
    client = ProductClient()
    return Response(client.list_products())
