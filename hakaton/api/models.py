from django.db import models


class Shops(models.Model):
    """Модель магазинов"""
    store = models.CharField(verbose_name='Название магазина',
                             max_length=200, unique=True)
    city = models.CharField(verbose_name='Город', max_length=200)
    divizion = models.CharField(verbose_name='Дивизион', max_length=200)
    format = models.SlugField(verbose_name='Формат магазина',
                              max_length=200, unique=True)
    loc = models.SlugField(verbose_name='Локация магазина',
                           max_length=200, unique=True)
    size = models.SlugField(verbose_name='Тип размера магазина',
                            max_length=200, unique=True)
    is_active = models.BooleanField(
        verbose_name='Флаг активного магазина')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.store


class Categories(models.Model):
    """Модель категорий"""
    sku = models.CharField(verbose_name='Наименование товара ',
                           max_length=200)
    group = models.CharField(verbose_name='Группа товара ',
                             max_length=200)
    category = models.CharField(verbose_name='Категория товара',
                                max_length=200)
    subcategory = models.CharField(verbose_name='Подкатегория товара',
                                   max_length=200)
    uom = models.PositiveIntegerField(
        verbose_name='Маркер товара -на вес или шт')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.sku


class Sales(models.Model):
    """Модель продаж"""
    store = models.ForeignKey(
        Shops, on_delete=models.CASCADE,
        related_name='sales',
        verbose_name='магазин'
    )
    sku = models.ForeignKey(
        Categories, on_delete=models.CASCADE,
        related_name='sales',
        verbose_name='товар'
    )

    date = models.DateField(verbose_name='Дата продажи товара')
    sales_type = models.PositiveIntegerField(verbose_name='Флаг наличия промо')
    sales_units = models.PositiveIntegerField(
        verbose_name='Число проданных товаров без признака промо')
    sales_units_promo = models.PositiveIntegerField(
        verbose_name='Число проданных товаров c признаком промо')
    sales_rub = models.FloatField(
        verbose_name='Цена проданных товаров без признака промо')
    sales_rub_promo = models.FloatField(
        verbose_name='Цена проданных товаров c признаком промо')

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return (f'{self.date} {self.sales_type}'
                f'{self.sales_units} {self.sales_units_promo}'
                f'{self.sales_rub} {self.sales_rub_promo}')


class Forecast(models.Model):
    """Модель прогноза продаж."""

    store = models.ForeignKey(
        Shops, on_delete=models.CASCADE,
        related_name='forecast',
        verbose_name='магазин'
    )
    sku = models.ForeignKey(
        Categories, on_delete=models.CASCADE,
        related_name='forecast',
        verbose_name='товар'
    )
    forecast_date = models.DateField(verbose_name='Дата отчета')
    date = models.DateField(verbose_name='Дата прогноза продажи')
    sales_units = models.PositiveIntegerField(
        verbose_name='Прогнозируемый спрос в шт',
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'Прогноз продаж'
        verbose_name_plural = 'Прогноз продаж'

    def __str__(self):
        return (f'{self.date}:{self.sales_units}')
