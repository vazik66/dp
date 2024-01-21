from django.db import models
from products.models import Product


class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    question_text = models.TextField("Question")
    author_name = models.CharField("Author name", max_length=64)
    author_url = models.URLField("Author url", blank=True)
    question_url = models.URLField("Question url", blank=True)

    asked_at = models.DateTimeField("Question asked at")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
