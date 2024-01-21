from django.contrib import admin
from .models import Manager


@admin.register(Manager)
class ManagerAdminModel(admin.ModelAdmin):
    list_display = [
        "seller",
        "telegram_username",
        "telegram_user_id",
        "updated_at",
        "created_at",
    ]
