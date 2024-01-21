from django.db import models
from sellers.models import Seller


class Manager(models.Model):
    # TODO: Telegram bot invite link with extra params ?
    # Either send invite
    # Or generate code to paste to bot, in order to get permission
    # Group chats

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    telegram_user_id = models.CharField("Telegram user id", max_length=255, blank=True)
    telegram_username = models.CharField(
        "Telegram username", max_length=64, db_index=True
    )
    telegram_chat_id = models.CharField(
        "Telegram chat id", max_length=16, db_index=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.telegram_username}"


# class SubscriptionPlan(models.Model):
#     pass
