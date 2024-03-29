# Generated by Django 5.0 on 2023-12-16 08:54

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sellers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(max_length=256, verbose_name="Product name"),
                ),
                ("product_url", models.URLField()),
                ("product_sku", models.CharField(max_length=64)),
                (
                    "marketplace",
                    models.CharField(
                        choices=[
                            ("OZON", "Ozon"),
                            ("YANDEX_MARKET", "Yandex market"),
                            ("WILDBERRIES", "Wildberries"),
                        ],
                        max_length=64,
                    ),
                ),
                (
                    "last_questions_parsed_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            1900, 1, 1, 0, 0, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sellers.seller"
                    ),
                ),
            ],
        ),
    ]
