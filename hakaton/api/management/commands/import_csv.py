import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from products.models import Category, Forecast, Product, Sale, Shop, Store


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
                new_item = Shop(
                    store=Store.objects.get_or_create(hash_id=st_id)[0],
                    city=st_city_id,
                    divizion=st_division_code,
                    format=st_type_format_id,
                    loc=st_type_loc_id,
                    size=st_type_size_id,
                    is_active=st_is_active,
                )
                to_import.append(new_item)
            Shop.objects.bulk_create(to_import)
            print(f"Файл {csv_file1.name} загружен.")

        csv_file2 = settings.BASE_DIR / "data" / "pr_df.csv"
        with open(csv_file2, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            to_import = []
            for row in reader:
                (pr_sku_id, pr_group_id, pr_cat_id, pr_subcat_id, pr_uom_id) = row
                new_item = Category(
                    sku=Product.objects.get_or_create(hash_id=pr_sku_id)[0],
                    group=pr_group_id,
                    category=pr_cat_id,
                    subcategory=pr_subcat_id,
                    uom=pr_uom_id,
                )
                to_import.append(new_item)
            Category.objects.bulk_create(to_import)
            print(f"Файл {csv_file2.name} загружен.")

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
            print(f"Файл {csv_file3.name} загружен.")

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
            print(f"Файл {csv_file4.name} загружен.")
