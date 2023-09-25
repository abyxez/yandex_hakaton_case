import django_filters as filters
from models import (Categories, Shops, Sales, Forecast)


class SalesFilter(filters.FilterSet):
    """Фильтры для продаж. """

    class Meta:
        model = Sales
        fields = ('sku', 'store',)


class CategoriesFilter(filters.FilterSet):
    """Фильтр для категорий"""

    class Meta:
        model = Categories
        fields = ('sku', 'group', 'category', 'subcategory',)


class ShopsFilter(filters.FilterSet):
    """Фильтр для магазинов"""

    class Meta:
        model = Shops
        fields = ('store', 'city', 'divizion',
                  'format', 'loc', 'size', 'is_active',)


class ForecastFilter(filters.FilterSet):
    """Фильтр для прогноза товара"""

    class Meta:
        model = Forecast
        fields = ('store', 'sku', 'forecast_date',)
