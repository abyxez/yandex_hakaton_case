from django.contrib.admin import ModelAdmin, register

from products.models import Category, Forecast, Sale, City, Division, Subcategory, Format, Location, ProductStore, Excel, Size, Store, ShoppingMall


@register(ShoppingMall)
class Shop(ModelAdmin):
    """Настройки для админ зоны магазинов"""

    list_display = (
        "id",
        "store",
        "city",
        "division",
        "format",
        "location",
        "size",
        "is_active",
    )
    search_fields = (
        "store",
    )
    list_filter = (
        "store",
        "city",
        "division",
        "format",
        "location",
        "size",
        "is_active",
    )
    empty_value_display = "-empty-"


@register(ProductStore)
class ProductAdmin(ModelAdmin):
    """
    Настройки для админ зоны категорий.
    """

    list_display = (
        "id",
        "sku",
        "group",
        "category",
        "subcategory",
        "uom",
    )
    search_fields = ("sku",)
    list_filter = (
        "sku",
        "group",
        "category",
        "subcategory",
    )
    empty_value_display = "-empty-"


@register(Sale)
class SaleAdmin(ModelAdmin):
    """
    Настройки для админ зоны продаж.
    """

    list_display = (
        "id",
        "store",
        "sku",
        "date",
        "sales_type",
        "sales_units",
        "sales_units_promo",
        "sales_rub",
        "sales_rub_promo",
    )
    search_fields = (
        "store",
        "sku",
    )
    list_filter = (
        "store",
        "sku",
        "date",
        "sales_type",
    )
    empty_value_display = "-empty-"


@register(Forecast)
class ForecastAdmin(ModelAdmin):
    """
    Настройки для админ зоны прогноза продаж.
    """

    list_display = (
        "id",
        "store",
        "sku",
        "date",
        "sales_units",
    )
    search_fields = (
        "store",
        "sku",
    )
    list_filter = ("store", "sku", "date")
    empty_value_display = "-пусто-"


