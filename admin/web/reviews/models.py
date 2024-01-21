from django.db import models
from products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField("Review")

    author_name = models.CharField("Author name", max_length=64)
    author_url = models.URLField("Author url", blank=True)
    review_url = models.URLField("Review url", blank=True)
    sent_at = models.DateTimeField("Review sent at")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
