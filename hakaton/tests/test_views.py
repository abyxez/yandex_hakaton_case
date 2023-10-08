from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from http import HTTPStatus


from products.models import Category, Forecast, Sale, Shop, Product, Store
User = get_user_model()


class ProductModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='TestUser')
        cls.sku = Product.objects.create(
            hash_id='Тестовый hash',
            name='test-name',
        )
        cls.category = Category.objects.create(
            sku_id=cls.sku.id,
            group='test-group',
            category='test-category',
            subcategory='test-subcategory',
            uom='1'
        )
        cls.store = Store.objects.create(
            hash_id='Тестовый hash',
            name='test-name',
        )
        cls.shop = Shop.objects.create(
            store_id=cls.store.id,
            city='test-city',
            divizion='test-divizion',
            format='1',
            loc='1',
            size='1',
            is_active='1',
        )
        cls.sale = Sale.objects.create(
            store_id=cls.store.id,
            sku_id=cls.sku.id,
            date='2023-10-05',
            sales_type='1',
            sales_units='1',
            sales_units_promo='1',
            sales_rub='1',
            sales_rub_promo='1',
        )
        cls.forecast = Forecast.objects.create(
            store_id=cls.store.id,
            sku_id=cls.sku.id,
            date='2023-10-10',
            sales_units='1',
        )

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_categories_list(self):
        """Контекст - список товаров."""
        response = self.guest_client.get(reverse('api:categories-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_shops_list(self):
        """Контекст - список магазинов."""
        response = self.guest_client.get(reverse('api:shops-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_sales_list(self):
        """Контекст - список продаж."""
        response = self.guest_client.get(reverse('api:sales-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_forecasts_list(self):
        """Контекст - список продаж."""
        response = self.guest_client.get(reverse('api:forecast-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_users_list(self):
        """Контекст - список пользователей."""
        response = self.guest_client.get(reverse('api:users-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data['results']), 1)
