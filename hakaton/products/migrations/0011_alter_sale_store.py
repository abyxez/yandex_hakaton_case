# Generated by Django 4.2.5 on 2023-09-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0010_alter_sale_sales_units_alter_sale_sales_units_promo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="store",
            field=models.CharField(max_length=200, verbose_name="магазин"),
        ),
    ]