# Generated by Django 5.0.9 on 2024-10-26 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("amazon", "0004_rnr_marketplace"),
    ]

    operations = [
        migrations.CreateModel(
            name="Promotions",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("deleted_on", models.DateTimeField(blank=True, null=True)),
                ("asin", models.CharField(max_length=10)),
                ("brand", models.CharField(blank=True, max_length=255, null=True)),
                ("deal_badge", models.CharField(blank=True, max_length=255, null=True)),
                ("deal_text", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "discount_percentage",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("listing_image", models.URLField(blank=True, null=True)),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "prime_benefit_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "prime_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "promotion_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "parent_rating",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("parent_total_reviews", models.IntegerField(blank=True, null=True)),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "marketplace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="amazon.marketplace",
                    ),
                ),
            ],
            options={
                "verbose_name": "Promotions",
                "verbose_name_plural": "Promotions",
                "db_table": '"amazon"."promotions"',
            },
        ),
    ]
