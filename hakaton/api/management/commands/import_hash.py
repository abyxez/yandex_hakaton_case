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
        """
        Вспомогательный импорт хэшированных ид в
        промежуточные таблицы по товарам и магазинам.
        """
        csv_file1 = settings.BASE_DIR / "data" / "pr_df.csv"
        with open(csv_file1, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                hashes.append(row[0])
            to_create = []
            for hash in set(hashes):
                new_item = Product(hash_id=hash)
                to_create.append(new_item)
            Product.objects.bulk_create(to_create)
            print("Список hash_id-id для продуктов загружен.")

        csv_file2 = settings.BASE_DIR / "data" / "st_df.csv"
        with open(csv_file2, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (st_id,st_city_id,st_division_code,st_type_format_id,st_type_loc_id,st_type_size_id,st_is_active) = row
                hashes.append(row[0])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Store(hash_id=hash)
                to_create.append(new_item)
            Store.objects.bulk_create(to_create)
            print("Список hash_id-id для магазинов загружен.")

        csv_file3 = settings.BASE_DIR / "data" / "pr_df.csv"
        with open(csv_file3, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (pr_sku_id,pr_group_id,pr_cat_id,pr_subcat_id,pr_uom_id) = row
                hashes.append(row[2])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Category(hash_id=hash)
                to_create.append(new_item)
            Category.objects.bulk_create(to_create)
            print("Список hash_id-id для категорий загружен.")

        csv_file4 = settings.BASE_DIR / "data" / "pr_df.csv"
        with open(csv_file4, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (pr_sku_id,pr_group_id,pr_cat_id,pr_subcat_id,pr_uom_id) = row
                hashes.append(row[3])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Subcategory(hash_id=hash)
                to_create.append(new_item)
            Subcategory.objects.bulk_create(to_create)
            print("Список hash_id-id для подкатегорий загружен.")

        csv_file5 = settings.BASE_DIR / "data" / "pr_df.csv"
        with open(csv_file5, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (pr_sku_id,pr_group_id,pr_cat_id,pr_subcat_id,pr_uom_id) = row
                hashes.append(row[1])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Group(hash_id=hash)
                to_create.append(new_item)
            Group.objects.bulk_create(to_create)
            print("Список hash_id-id для товарных групп загружен.")

        csv_file6 = settings.BASE_DIR / "data" / "st_df.csv"
        with open(csv_file6, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (st_id,st_city_id,st_division_code,st_type_format_id,st_type_loc_id,st_type_size_id,st_is_active) = row
                hashes.append(row[1])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = City(hash_id=hash)
                to_create.append(new_item)
            City.objects.bulk_create(to_create)
            print("Список hash_id-id для городов загружен.")

        csv_file7 = settings.BASE_DIR / "data" / "st_df.csv"
        with open(csv_file7, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (st_id,st_city_id,st_division_code,st_type_format_id,st_type_loc_id,st_type_size_id,st_is_active) = row
                hashes.append(row[2])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Division(hash_id=hash)
                to_create.append(new_item)
            Division.objects.bulk_create(to_create)
            print("Список hash_id-id для дивизионов загружен.")

        csv_file8 = settings.BASE_DIR / "data" / "st_df.csv"
        with open(csv_file8, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (st_id,st_city_id,st_division_code,st_type_format_id,st_type_loc_id,st_type_size_id,st_is_active) = row
                hashes.append(row[5])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Size(name=hash)
                to_create.append(new_item)
            Size.objects.bulk_create(to_create)
            print("Список размеров магазина загружен.")

        csv_file9 = settings.BASE_DIR / "data" / "st_df.csv"
        with open(csv_file7, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (st_id,st_city_id,st_division_code,st_type_format_id,st_type_loc_id,st_type_size_id,st_is_active) = row
                hashes.append(row[3])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Format(name=hash)
                to_create.append(new_item)
            Format.objects.bulk_create(to_create)
            print("Список форматов магазина загружен.")

        csv_file7 = settings.BASE_DIR / "data" / "st_df.csv"
        with open(csv_file7, "r", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            next(reader, None)
            hashes = []
            for row in reader:
                (st_id,st_city_id,st_division_code,st_type_format_id,st_type_loc_id,st_type_size_id,st_is_active) = row
                hashes.append(row[4])
            unique_import = set(hashes)
            to_create = []
            for hash in set(hashes):
                new_item = Location(name=hash)
                to_create.append(new_item)
            Location.objects.bulk_create(to_create)
            print("Список локаций загружен.")