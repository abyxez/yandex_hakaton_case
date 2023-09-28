import django_filters as filters
from products.models import (Category, Shop, Sale, Forecast)


class SaleFilter(filters.FilterSet):
    """Фильтры для продаж. """

    class Meta:
        model = Sale
        fields = ('sku', 'store',)


class CategoryFilter(filters.FilterSet):
    """Фильтр для категорий"""

    class Meta:
        model = Category
        fields = ('sku', 'group', 'category', 'subcategory',)


class ShopFilter(filters.FilterSet):
    """Фильтр для магазинов"""

    class Meta:
        model = Shop
        fields = ('store', 'city', 'divizion',
                  'format', 'loc', 'size', 'is_active',)


class ForecastFilter(filters.FilterSet):
    """Фильтр для прогноза товара"""

    class Meta:
        model = Forecast
        fields = ('store', 'sku', )
