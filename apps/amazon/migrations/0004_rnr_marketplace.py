# Generated by Django 5.0.9 on 2024-10-26 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("amazon", "0003_rnr"),
    ]

    operations = [
        migrations.AddField(
            model_name="rnr",
            name="marketplace",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="amazon.marketplace",
            ),
        ),
    ]
