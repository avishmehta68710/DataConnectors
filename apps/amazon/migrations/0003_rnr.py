# Generated by Django 5.0.9 on 2024-10-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("amazon", "0002_inventory"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rnr",
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
                ("asin", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "child_one_star_reviews_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_one_star_rating_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_two_star_reviews_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_two_star_rating_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_three_star_reviews_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_three_star_rating_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_four_star_reviews_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_four_star_rating_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_five_star_reviews_count",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "child_five_star_rating_count",
                    models.IntegerField(blank=True, null=True),
                ),
                ("child_total_rating", models.IntegerField(blank=True, null=True)),
                ("child_total_reviews", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Rating And Reviews",
                "verbose_name_plural": "Rating And Reviews",
                "db_table": '"amazon"."rnr"',
            },
        ),
    ]