import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from products.models import (
    Category,
    City,
    Division,
    Excel,
    Forecast,
    Format,
    Location,
    Product,
    ProductStore,
    Sale,
    ShoppingMall,
    Size,
    Store,
    Subcategory,
    Group,
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_file1 = settings.BASE_DIR / "data" / "st_df.csv"
        with open(csv_file1, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            to_import = []
            for row in reader:
                (
                    st_id,
                    st_city_id,
                    st_division_code,
                    st_type_format_id,
                    st_type_loc_id,
                    st_type_size_id,
                    st_is_active,
                ) = row
                new_item = ShoppingMall(
                    store=Store.objects.get_or_create(hash_id=st_id)[0],
                    city=City.objects.get_or_create(hash_id=st_city_id)[0],
                    division=Division.objects.get_or_create(hash_id=st_division_code)[0],
                    format=Format.objects.get_or_create(name=st_type_format_id)[0],
                    location=Location.objects.get_or_create(name=st_type_loc_id)[0],
                    size=Size.objects.get_or_create(name=st_type_size_id)[0],
                    is_active=st_is_active,
                )
                to_import.append(new_item)
            ShoppingMall.objects.bulk_create(to_import)
            print(f"Список магазинов загружен.")

        csv_file2 = settings.BASE_DIR / "data" /"pr_df_updated.csv"
        with open(csv_file2, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            to_import = []
            for row in reader:
                (st_id,pr_sku_id,pr_group_id,pr_cat_id,pr_subcat_id,pr_uom_id) = row
                new_item = ProductStore(
                    sku=Product.objects.get_or_create(hash_id=pr_sku_id)[0],
                    store=Store.objects.get_or_create(hash_id=st_id)[0],
                    group=Group.objects.get_or_create(hash_id=pr_group_id)[0],
                    category=Category.objects.get_or_create(hash_id=pr_cat_id)[0],
                    subcategory=Subcategory.objects.get_or_create(hash_id=pr_subcat_id)[0],
                    uom=pr_uom_id,
                )
                to_import.append(new_item)
            ProductStore.objects.bulk_create(to_import)
            print(f"Список магазинов, товаров и категорий загружен.")

        csv_file3 = settings.BASE_DIR / "data" / "sales_df_train.csv"
        with open(csv_file3, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            to_import = []
            for row in reader:
                (
                    st_id,
                    pr_sku_id,
                    date,
                    pr_sales_type_id,
                    pr_sales_in_units,
                    pr_promo_sales_in_units,
                    pr_sales_in_rub,
                    pr_promo_sales_in_rub,
                ) = row
                new_item = Sale(
                    store=Store.objects.filter(hash_id=st_id)[0],
                    sku=Product.objects.filter(hash_id=pr_sku_id)[0],
                    date=date,
                    sales_type=pr_sales_type_id,
                    sales_units=pr_sales_in_units,
                    sales_units_promo=pr_promo_sales_in_units,
                    sales_rub=pr_sales_in_rub,
                    sales_rub_promo=pr_promo_sales_in_rub,
                )
                to_import.append(new_item)
            Sale.objects.bulk_create(to_import)
            print(f"Статистика продаж загружена.")

        csv_file4 = settings.BASE_DIR / "data" / "sales_submission.csv"
        with open(csv_file4, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            to_import = []
            for row in reader:
                (st_id, pr_sku_id, date, target) = row
                new_item = Forecast(
                    store=Store.objects.filter(hash_id=st_id)[0],
                    sku=Product.objects.filter(hash_id=pr_sku_id)[0],
                    date=date,
                    sales_units=target,
                )
                to_import.append(new_item)
            Forecast.objects.bulk_create(to_import)
            print(f"Прогноз продаж загружен.")
