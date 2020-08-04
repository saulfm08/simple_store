from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

class CategoryAdmin(admin.ModelAdmin):
    list_display  = ["name", "description"]
    search_fields = ["name", "description"]


class Product(models.Model):
    name          = models.CharField(max_length=200)
    url           = models.TextField(null=True, blank=True)
    image         = models.ImageField(upload_to="products")
    description   = models.TextField(null=True, blank=True)
    category      = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    created       = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated       = models.DateTimeField(auto_now=True, null=True, blank=True)  


    def __str__(self):
        return self.name

class ProductAdmin(admin.ModelAdmin):
    list_display  = [ "id", "name", "category", "created", "updated"]
    search_fields = ["name", "category"]

