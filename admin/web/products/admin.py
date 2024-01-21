from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = [
        "product_sku",
        "product_name",
        "product_url",
        "marketplace",
        "last_questions_parsed_at",
        "created_at",
        "seller",
    ]
