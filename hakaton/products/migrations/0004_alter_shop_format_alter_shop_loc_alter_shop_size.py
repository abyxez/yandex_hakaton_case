# Generated by Django 4.2.5 on 2023-09-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_alter_shop_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="format",
            field=models.SlugField(max_length=200, verbose_name="Формат магазина"),
        ),
        migrations.AlterField(
            model_name="shop",
            name="loc",
            field=models.SlugField(max_length=200, verbose_name="Локация магазина"),
        ),
        migrations.AlterField(
            model_name="shop",
            name="size",
            field=models.SlugField(max_length=200, verbose_name="Тип размера магазина"),
        ),
    ]