import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from products.models import Excel, Product, Store


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_file1 = settings.BASE_DIR / "data_with_weeks_fillna.csv"
        with open(csv_file1, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            to_import = []
            # i = 0
            for row in reader:
                (
                    st_id,
                    pr_sku_id,
                    date,
                    total_sales_in_units,
                    target,
                    week,
                    pr_cat_id,
                    pr_subcat_id,
                ) = row
                try:
                    if target == "" or total_sales_in_units == "":
                        target, total_sales_in_units, difference, wape = (
                            None,
                            None,
                            None,
                            None,
                        )
                    else:
                        difference = abs(float(total_sales_in_units) - float(target))
                        wape = abs(float(total_sales_in_units) - float(target)) / float(
                            target
                        )

                    new_item = Excel(
                        store=Store.objects.get_or_create(hash_id=st_id)[0],
                        category=pr_cat_id,
                        subcategory=pr_subcat_id,
                        sku=Product.objects.get_or_create(hash_id=pr_sku_id)[0],
                        week=week,
                        sales_units=total_sales_in_units,
                        target=target,
                        difference=difference,
                        wape=wape,
                    )
                    to_import.append(new_item)

                    # print(i/750000)
                    # i+= 1
                except (ZeroDivisionError, ValueError) as e:
                    target, total_sales_in_units, difference, wape = (
                        None,
                        None,
                        None,
                        None,
                    )

            Excel.objects.bulk_create(to_import)
            print(f"Таблица products_excel успешно заполнена!")
