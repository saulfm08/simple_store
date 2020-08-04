from django.conf import settings
from product.models import Product

class ProductClient():
    def __init__(self):
        print("Print __init__ stage")

    def list_products(self):
        products = Product.objects.all().order_by("updated")
        return products
