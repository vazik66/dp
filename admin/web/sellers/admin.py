from django.contrib import admin
from .models import Seller, OzonCredential, WildberriesCredential, YandexMarketCredential


@admin.register(Seller)
class SellerAdminView(admin.ModelAdmin):
    list_display = ["telegram_username", "telegram_user_id", "updated_at", "created_at"]


@admin.register(OzonCredential)
class OzonCredentialsAdminView(admin.ModelAdmin):
    list_display = ["seller", "api_key", "client_id", "created_at", "updated_at"]


@admin.register(WildberriesCredential)
class WildebrriesCredentialsAdminView(admin.ModelAdmin):
    list_display = ["seller", "api_key", "created_at", "updated_at"]


@admin.register(YandexMarketCredential)
class YandexMarketCredentialsAdminView(admin.ModelAdmin):
    list_display = ["seller", "api_key", "created_at", "updated_at"]
