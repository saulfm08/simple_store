from django.db import models
from django.contrib import admin

class Product(models.Model):
    name = models.CharField(max_length=200)

    url = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="products")
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

class ProductAdmin(admin.ModelAdmin):
    list_display  = ["name", "url", "image", "description"]
    search_fields = ["name", "url", "image", "description"]