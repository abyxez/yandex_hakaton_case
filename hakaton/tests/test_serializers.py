from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from api.serializers import (ForecastGetSerializer,SaleSerializer,
                             ShoppingMallSerializer,ProductStoreSerializer)
from products.models import (Category, Forecast, Product, Sale, Store, Subcategory, Group, City, Division, Format, Location, Size, ShoppingMall, ProductStore)

User = get_user_model()


class ProductSerializersTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username="TestUser")
        cls.sku = Product.objects.create(
            hash_id="Тестовый товар",
            name="test-sku",
        )
        cls.store = Store.objects.create(
            hash_id="Тестовый магазин",
            name="test-store"
        )
        cls.group = Group.objects.create(
            hash_id="Тестовая группа товара",
            name="test-group",
        )
        cls.category = Category.objects.create(
            hash_id="Тестовая категория товара",
            name="test-category",
        )
        cls.subcategory = Subcategory.objects.create(
            hash_id="Тестовая субкатегория товара",
            name="test-subcategory",
        )
        cls.city = City.objects.create(
            hash_id="Тестовый город магазина ",
            name="test-city",
        )
        cls.division = Division.objects.create(
            hash_id="Тестовый дивизион магазина",
            name="test-division",
        )
        cls.format = Format.objects.create(
            name="test-format",
        )
        cls.location = Location.objects.create(
            name="test-location",
        )
        cls.size = Size.objects.create(
            name="test-location",
        )  
        cls.shoppingmall = ShoppingMall.objects.create(
            store_id=cls.store.id,
            city_id=cls.city.id,
            division_id=cls.division.id,
            format_id=cls.format.id,
            location_id=cls.location.id,
            size_id=cls.size.id,
            is_active="1",
        )
        cls.producrstore = ProductStore.objects.create(
            store_id=cls.store.id,
            sku_id=cls.sku.id,
            group_id=cls.group.id,
            category_id=cls.category.id,
            subcategory_id=cls.subcategory.id,
            uom="1",
        )
        cls.sale = Sale.objects.create(
            store_id=cls.store.id,
            sku_id=cls.sku.id,
            date="2023-10-05",
            sales_type="1",
            sales_units="1",
            sales_units_promo="1",
            sales_rub="1",
            sales_rub_promo="1",
        )
        cls.forecast = Forecast.objects.create(
            store_id=cls.store.id,
            sku_id=cls.sku.id,
            date="2023-10-10",
            sales_units="1",
        )


    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_sale_serializer(self):
        val_dict = {
            "store": "1",
            "sku": "1",
            "group": "test-group",
            "category": "test-category",
            "subcategory": "test-subcategory",
            "uom": "1",
        }
        serializer = SaleSerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())

    def test_shoppingmall_serializer(self):
        val_dict = {
            "store": "1",
            "city": "1",
            "division": "1",
            "format": "1",
            "location": "1",
            "size": "1",
            "is_active": "1",
        }
        serializer = ShoppingMallSerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())

    def test_productstore_serializer(self):
        val_dict = {
            "store": "1",
            "sku": "1",
            "group": "1",
            "category": "1",
            "subcategory": "1",
            "uom": "1",
            "date": "2023-10-05",
            "sales_units": "1",
        }
        serializer = ProductStoreSerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())

    def test_forecast_serializer(self):
        val_dict = {"store": "1", "sku": "1", "date": "2023-10-05", "sales_units": "1"}
        serializer = ForecastGetSerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())
