from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from products.models import (Category, Forecast, Product, Sale, Store, 
                             Subcategory, Group, City, Division, Format, 
                             Location, Size, ShoppingMall, ProductStore)

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

    def test_categories_list(self):
        """Контекст - список товаров."""
        response = self.guest_client.get(reverse("api:categories-list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_shops_list(self):
        """Контекст - список магазинов."""
        response = self.guest_client.get(reverse("api:shops-list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_sales_list(self):
        """Контекст - список продаж."""
        response = self.guest_client.get(reverse("api:sales-list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_forecasts_list(self):
        """Контекст - список прогнозов."""
        response = self.guest_client.get(reverse("api:forecast-list"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data["results"]), 1)
