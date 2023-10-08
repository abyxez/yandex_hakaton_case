import django_filters as filters

from products.models import (
    Category,
    City,
    Division,
    Excel,
    Forecast,
    Format,
    Location,
    ProductStore,
    Sale,
    ShoppingMall,
    Size,
    Store,
    Subcategory,
)


class SaleFilter(filters.FilterSet):
    """Фильтры для продаж."""

    class Meta:
        model = Sale
        fields = (
            "sku",
            "store",
        )


class CategoryFilter(filters.FilterSet):
    """Фильтр для категорий"""

    class Meta:
        model = ProductStore
        fields = (
            "sku",
            "group",
            "category",
            "subcategory",
        )


class ShopFilter(filters.FilterSet):
    """Фильтр для магазинов"""

    class Meta:
        model = ShoppingMall
        fields = (
            "store",
            "city",
            "division",
            "format",
            "location",
            "size",
            "is_active",
        )


class ForecastFilter(filters.FilterSet):
    """Фильтр для прогноза товара"""

    class Meta:
        model = Forecast
        fields = (
            "store",
            "sku",
        )
