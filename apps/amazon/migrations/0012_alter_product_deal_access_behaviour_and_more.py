# Generated by Django 5.0.9 on 2024-11-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0011_alter_product_deal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deal_access_behaviour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='deal_state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
