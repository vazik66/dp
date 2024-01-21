from django.db import models
from sellers.models import Seller
from datetime import datetime, timezone


MARKETPLACES = {
    "OZON": "Ozon",
    "YANDEX_MARKET": "Yandex market",
    "WILDBERRIES": "Wildberries",
}


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name = models.CharField("Product name", max_length=256)
    product_url = models.URLField()
    product_sku = models.CharField(max_length=64)
    marketplace = models.CharField(choices=MARKETPLACES, max_length=64)
    last_questions_parsed_at = models.DateTimeField(
        default=datetime(1900, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product_name
