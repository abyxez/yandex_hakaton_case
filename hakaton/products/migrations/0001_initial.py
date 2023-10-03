# Generated by Django 4.2.5 on 2023-10-02 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Название товара",
                    ),
                ),
                (
                    "hash_id",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Хэшированный ID"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Store",
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
                    "name",
                    models.CharField(
                        blank=True,
                        default="Лента",
                        max_length=200,
                        null=True,
                        verbose_name="Название магазина",
                    ),
                ),
                (
                    "hash_id",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Хэшированный ID"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Shop",
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
                ("city", models.CharField(max_length=200, verbose_name="Город")),
                ("divizion", models.CharField(max_length=200, verbose_name="Дивизион")),
                ("format", models.IntegerField(verbose_name="Формат магазина")),
                ("loc", models.IntegerField(verbose_name="Локация магазина")),
                ("size", models.IntegerField(verbose_name="Тип размера магазина")),
                (
                    "is_active",
                    models.IntegerField(verbose_name="Флаг активного магазина"),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shops",
                        to="products.store",
                        verbose_name="Магазин",
                    ),
                ),
            ],
            options={
                "verbose_name": "Магазин",
                "verbose_name_plural": "Магазины",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Sale",
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
                    "date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата продажи товара"
                    ),
                ),
                (
                    "sales_type",
                    models.PositiveIntegerField(verbose_name="Флаг наличия промо"),
                ),
                (
                    "sales_units",
                    models.FloatField(
                        verbose_name="Число проданных товаров без признака промо"
                    ),
                ),
                (
                    "sales_units_promo",
                    models.FloatField(
                        verbose_name="Число проданных товаров c признаком промо"
                    ),
                ),
                (
                    "sales_rub",
                    models.FloatField(
                        verbose_name="Цена проданных товаров без признака промо"
                    ),
                ),
                (
                    "sales_rub_promo",
                    models.FloatField(
                        verbose_name="Цена проданных товаров c признаком промо"
                    ),
                ),
                (
                    "sku",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sales",
                        to="products.product",
                        verbose_name="товар",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sales",
                        to="products.store",
                        verbose_name="магазин",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продажа",
                "verbose_name_plural": "Продажи",
                "ordering": ("-date",),
            },
        ),
        migrations.CreateModel(
            name="Forecast",
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
                ("date", models.DateField(verbose_name="Дата прогноза продажи")),
                (
                    "sales_units",
                    models.PositiveIntegerField(
                        verbose_name="Прогнозируемый спрос в шт"
                    ),
                ),
                (
                    "sku",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forecast",
                        to="products.product",
                        verbose_name="товар",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forecasts",
                        to="products.store",
                        verbose_name="магазин",
                    ),
                ),
            ],
            options={
                "verbose_name": "Прогноз продаж",
                "verbose_name_plural": "Прогноз продаж",
                "ordering": ("date",),
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                    "group",
                    models.CharField(max_length=200, verbose_name="Группа товара "),
                ),
                (
                    "category",
                    models.CharField(max_length=200, verbose_name="Категория товара"),
                ),
                (
                    "subcategory",
                    models.CharField(
                        max_length=200, verbose_name="Подкатегория товара"
                    ),
                ),
                (
                    "uom",
                    models.IntegerField(verbose_name="Маркер товара -на вес или шт"),
                ),
                (
                    "sku",
                    models.ForeignKey(
                        max_length=200,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="Наименование товара ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("id",),
            },
        ),
    ]
