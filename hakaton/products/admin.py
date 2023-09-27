from django.contrib import admin


from products.models import (Categories, Shops, Sales, Forecast)


class ShopsAdmin(admin.ModelAdmin):
    """Настройки для админ зоны магазинов"""
    list_display = ('id', 'store', 'city', 'divizion',
                    'format', 'loc', 'size', 'is_active',)
    search_fields = ('store', 'slug',)
    list_filter = ('store', 'city', 'divizion',
                   'format', 'loc', 'size', 'is_active',)
    empty_value_display = '-empty-'


class CategoriesAdmin(admin.ModelAdmin):
    """
    Настройки для админ зоны категорий.
    """
    list_display = ('id', 'sku', 'group', 'category', 'subcategory', 'uom',)
    search_fields = ('sku',)
    list_filter = ('sku', 'group', 'category', 'subcategory',)
    empty_value_display = '-empty-'


class SalesAdmin(admin.ModelAdmin):
    """
    Настройки для админ зоны продаж.
    """
    list_display = ('id', 'store', 'sku', 'date',
                    'sales_type', 'sales_units', 'sales_units_promo',
                    'sales_rub', 'sales_rub_promo',)
    search_fields = ('store', 'sku',)
    list_filter = ('store', 'sku', 'date', 'sales_type',)
    empty_value_display = '-empty-'


class ForecastAdmin(admin.ModelAdmin):
    """
    Настройки для админ зоны прогноза продаж.
    """

    list_display = ('id', 'store', 'sku', 'forecast_date',
                    'date', 'sales_units',)
    search_fields = ('store', 'sku',)
    list_filter = ('store', 'sku', 'forecast_date', 'date')
    empty_value_display = '-пусто-'


admin.site.register(Shops, ShopsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Forecast, ForecastAdmin)

