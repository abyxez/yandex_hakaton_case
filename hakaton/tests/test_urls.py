from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from products.models import Category, Forecast, Product, Sale, Shop, Store

User = get_user_model()


class ProductURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username="TestUser")
        cls.sku = Product.objects.create(
            hash_id="Тестовый hash",
            name="test-name",
        )
        cls.category = Category.objects.create(
            sku_id=cls.sku.id,
            group="test-group",
            category="test-category",
            subcategory="test-category",
            uom="1",
        )
        cls.store = Store.objects.create(
            hash_id="Тестовый hash",
            name="test-name",
        )
        cls.shop = Shop.objects.create(
            store_id=cls.store.id,
            city="test-city",
            divizion="test-divizion",
            format="1",
            loc="1",
            size="1",
            is_active="1",
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

    def test_urls_exists(self):
        """URL-доступны."""
        templates_url_exists = {
            "/api/categories/": HTTPStatus.OK,
            # f'/categories/{self.sku.pk}/': HTTPStatus.OK,
            "/api/shops/": HTTPStatus.OK,
            "/api/sales/": HTTPStatus.OK,
            "/api/forecast/": HTTPStatus.OK,
            "/api/unexisting_page/": HTTPStatus.NOT_FOUND,
            # '/categories/unexisting_category/': HTTPStatus.NOT_FOUND,
        }

        for url, code_response in templates_url_exists.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, code_response)
