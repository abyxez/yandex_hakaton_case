# Generated by Django 4.2.5 on 2023-09-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_alter_category_sku_alter_forecast_sku"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="date",
            field=models.CharField(max_length=200, verbose_name="Дата продажи товара"),
        ),
        migrations.AlterField(
            model_name="sale",
            name="sku",
            field=models.CharField(max_length=200, verbose_name="товар"),
        ),
    ]