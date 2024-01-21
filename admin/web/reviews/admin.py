from django.contrib import admin
from .models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdminView(admin.ModelAdmin):
    list_display = [
        "review_text",
        "product",
        "author_name",
        "author_url",
        "review_url",
        "created_at",
        "updated_at",
    ]
