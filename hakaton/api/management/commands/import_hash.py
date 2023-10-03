import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from products.models import Category, Forecast, Product, Sale, Shop, Store


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Вспомогательный импорт хэшированных ид в
        промежуточные таблицы по товарам и магазинам.
        """
        csv_file1 = settings.BASE_DIR / "data" / "sales_df_train.csv"
        with open(csv_file1, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                hashes.append(row[1])
            to_create = []
            for hash in set(hashes):
                new_item = Product(hash_id=hash)
                to_create.append(new_item)
            Product.objects.bulk_create(to_create)
            print("Список продуктов загружен.")

        csv_file2 = settings.BASE_DIR / "data" / "sales_df_train.csv"
        with open(csv_file2, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                # (st_id, pr_sku_id, date, target) = row
                hashes.append(row[0])
            # unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Store(hash_id=hash)
                to_create.append(new_item)
            Store.objects.bulk_create(to_create)
            print("Список магазинов загружен.")
