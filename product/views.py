from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from product.client import ProductClient

from django.core import serializers


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def product_list(request):
    client = ProductClient()
    return Response(client.list_products())

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def product_get(request, pk):
    client = ProductClient()
    return Response(client.get_product(pk))

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated & permissions.IsAdminUser])
def product_add(request):
    client = ProductClient()
    return Response(client.get_product(5))
