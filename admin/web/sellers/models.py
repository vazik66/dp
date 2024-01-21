from django.db import models


class Seller(models.Model):
    telegram_user_id = models.CharField("Telegram user id", max_length=255)
    telegram_username = models.CharField("Telegram username", max_length=64)
    telegram_chat_id = models.CharField(
        "Telegram chat id", max_length=16, db_index=True
    )

    # Ozon
    ozon_seller_id = models.CharField("Ozon seller id", max_length=16, blank=True, null=True)
    ozon_seller_url = models.CharField("Ozon seller url", max_length=512, blank=True, null=True)

    # Wildberries
    wildberries_seller_id = models.CharField(
        "Wildberries seller id", max_length=16, blank=True, null=True
    )
    wildberries_seller_url = models.CharField(
        "Wildberries seller url", max_length=512, blank=True, null=True
    )

    # Yandex Market
    yandex_market_seller_id = models.CharField(
        "Yandex Market seller id", max_length=16, blank=True, null=True
    )
    yandex_market_seller_url = models.CharField(
        "Yandex Market seller url", max_length=512, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.telegram_username}"


class OzonCredential(models.Model):
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    client_id = models.CharField("Ozon Client Id", max_length=64)
    api_key = models.CharField("Ozon API Key", max_length=36)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WildberriesCredential(models.Model):
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    api_key = models.CharField("Wildberries API Key", max_length=36)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class YandexMarketCredential(models.Model):
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    api_key = models.CharField("Yandex Market API Key", max_length=36)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
