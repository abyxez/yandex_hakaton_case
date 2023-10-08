from django.contrib.auth import get_user_model
from django.test import TestCase, Client

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

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        sku = ProductModelTest.sku
        category = ProductModelTest.category
        store = ProductModelTest.store
        shop = ProductModelTest.shop
        sale = ProductModelTest.sale
        forecast = ProductModelTest.forecast

        test_str = {
            sku.hash_id: str(sku),
            store.hash_id: str(store),
            # shop.store_id: str(shop),
            # category.sku_id: str(category),
            f"{shop.store} {shop.city} {shop.divizion} {shop.format} "
            f"{shop.loc} {shop.size} {shop.is_active}": str(shop),
            f"{category.sku} {category.group} {category.category} "
            f"{category.subcategory} {category.uom}": str(category),
            f"{sale.date} {sale.sales_type} {sale.sales_units} "
            f"{sale.sales_units_promo} {sale.sales_rub} "
            f"{sale.sales_rub_promo}": str(sale),
            f"{forecast.store} {forecast.sku} "
            f"{forecast.date} {forecast.sales_units}": str(forecast)
        }

        for field, expected_value in test_str.items():
            with self.subTest(field=field):
                response = field
                self.assertEqual(response, expected_value)
