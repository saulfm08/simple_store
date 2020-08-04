from django.conf import settings
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer


class ProductClient():
    def __init__(self):
        print("Print __init__ stage")

    def list_products(self):
        products = ProductSerializer(Product.objects.all().order_by("updated"), many=True)
        return products.data

    def get_product(self, pk):
        product = ProductSerializer(Product.objects.get(id=pk))
        return product.data
