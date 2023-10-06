from django.contrib.auth import get_user_model
from django.test import TestCase, Client


from products.models import Category, Forecast, Sale, Shop, Product, Store
from api.serializers import (
    CategorySerializer,
    ForecastGetSerializer,
    ForecastPostSerializer,
    SaleSerializer,
    ShopSerializer,
)
User = get_user_model()


class ProductSerializersTest(TestCase):
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

    def test_category_serializer(self):
        val_dict = {
            'sku': '1',
            'group': 'test-group',
            'category': 'test-category',
            'subcategory': 'test-subcategory',
            'uom': '1'}
        serializer = CategorySerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())

    def test_shop_serializer(self):
        val_dict = {
            'store': '1',
            'city': 'test-city',
            'divizion': 'test-divizion',
            'format': '1',
            'loc': '1',
            'size': '1',
            'is_active': '1'
            }
        serializer = ShopSerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())

    def test_sale_serializer(self):
        val_dict = {
            'store': '1',
            'sku': '1',
            'date': '2023-10-05',
            'sales_type': '1',
            'sales_units': '1',
            'sales_units_promo': '1',
            'sales_rub': '1',
            'sales_rub_promo': '1'
            }
        serializer = SaleSerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())

    def test_forecast_serializer(self):
        val_dict = {
            'store': '1',
            'sku': '1',
            'date': '2023-10-05',
            'sales_units': '1'
            }
        serializer = ForecastGetSerializer(data=val_dict)
        self.assertTrue(serializer.is_valid())
