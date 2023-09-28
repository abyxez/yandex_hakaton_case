from django.core.management.base import BaseCommand
from django.conf import settings
import csv
from products.models import Shop, Category, Sale, Forecast


class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_file1 = settings.BASE_DIR / 'data' / 'st_df.csv'
        with open(csv_file1, 'r', encoding="utf8") as f:
            x = csv.reader(f, delimiter=",")
            next(x, None)
            for row in x:
                (st_id, st_city_id, st_division_code, st_type_format_id,
                 st_type_loc_id, st_type_size_id, st_is_active) = row
                Shop.objects.get_or_create(
                    store=st_id, city=st_city_id, divizion=st_division_code,
                    format=st_type_format_id, loc=st_type_loc_id,
                    size=st_type_size_id, is_active=st_is_active
                )
            print(f'Файл {csv_file1.name} загружен.')

        csv_file2 = settings.BASE_DIR / 'data' / 'pr_df.csv'
        with open(csv_file2, 'r', encoding="utf8") as f:
            x = csv.reader(f, delimiter=",")
            next(x, None)
            for row in x:
                (pr_sku_id, pr_group_id, pr_cat_id,
                 pr_subcat_id, pr_uom_id) = row
                Category.objects.get_or_create(
                    sku=pr_sku_id, group=pr_group_id, category=pr_cat_id,
                    subcategory=pr_subcat_id, uom=pr_uom_id
                )
            print(f'Файл {csv_file2.name} загружен.')

        csv_file3 = settings.BASE_DIR / 'data' / 'sales_df_train.csv'
        with open(csv_file3, 'r', encoding="utf8") as f:
            x = csv.reader(f, delimiter=",")
            next(x, None)
            for row in x:
                (st_id, pr_sku_id, date, pr_sales_type_id,
                 pr_sales_in_units, pr_promo_sales_in_units,
                 pr_sales_in_rub, pr_promo_sales_in_rub) = row
                Sale.objects.get_or_create(
                    store=st_id, sku=pr_sku_id, date=date,
                    sales_type=pr_sales_type_id,
                    sales_units=pr_sales_in_units,
                    sales_units_promo=pr_promo_sales_in_units,
                    sales_rub=pr_sales_in_rub,
                    sales_rub_promo=pr_promo_sales_in_rub
                )
            print(f'Файл {csv_file3.name} загружен.')

        csv_file4 = settings.BASE_DIR / 'data' / 'sales_submission.csv'
        with open(csv_file4, 'r', encoding="utf8") as f:
            x = csv.reader(f, delimiter=",")
            next(x, None)
            for row in x:
                (st_id, pr_sku_id, date, target) = row
                Forecast.objects.get_or_create(
                    store=st_id, sku=pr_sku_id, date=date,
                    sales_units=target
                )
            print(f'Файл {csv_file4.name} загружен.')
