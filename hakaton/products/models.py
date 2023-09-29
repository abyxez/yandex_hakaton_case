from django.db import models
# from django.contrib.auth.models import AbstractUser


# class Product(models.Model):
#     name = models.CharField(
#         'Название продукта',
#         unique=True,
#         max_length=200,
#     )


class Shop(models.Model):
    """Модель магазинов"""
    store = models.CharField(verbose_name='Название магазина',
                             max_length=200, unique=True)
    city = models.CharField(verbose_name='Город', max_length=200)
    divizion = models.CharField(verbose_name='Дивизион', max_length=200)
    format = models.SlugField(verbose_name='Формат магазина',
                              max_length=200)
    loc = models.SlugField(verbose_name='Локация магазина',
                           max_length=200)
    size = models.SlugField(verbose_name='Тип размера магазина',
                            max_length=200)
    is_active = models.CharField(
        verbose_name='Флаг активного магазина', max_length=200)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.store


class Category(models.Model):
    """Модель категорий"""
    sku = models.CharField(
        'Наименование товара ',
        max_length=200,
    )
    group = models.CharField(verbose_name='Группа товара ',
                             max_length=200)
    category = models.CharField(verbose_name='Категория товара',
                                max_length=200)
    subcategory = models.CharField(verbose_name='Подкатегория товара',
                                   max_length=200)
    uom = models.SlugField(
        verbose_name='Маркер товара -на вес или шт')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.sku


class Sale(models.Model):
    """Модель продаж"""
    store = models.CharField(
        # Shop, on_delete=CASCADE,
        # related_name='sales',
        verbose_name='магазин',
        max_length=200,
    )
    sku = models.CharField(
        verbose_name='товар',
        max_length=200,
    )

    date = models.DateField(verbose_name='Дата продажи товара', blank=True, null=True)
    sales_type = models.PositiveIntegerField(verbose_name='Флаг наличия промо')
    sales_units = models.FloatField(
        verbose_name='Число проданных товаров без признака промо')
    sales_units_promo = models.FloatField(
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

    store = models.CharField(
        # Shop, on_delete=CASCADE,
        # related_name='forecast',
        verbose_name='магазин',
        max_length=200,
    )
    sku = models.CharField(
        # Product, on_delete=CASCADE,
        # related_name='forecast',
        verbose_name='товар',
        max_length=200,
    )
    # forecast_date = DateField(verbose_name='Дата отчета')
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


# class User(AbstractUser):
#     """Модель пользователей"""
#     username = models.CharField(
#         verbose_name='Имя пользователя',
#         validators=(validate_username,),
#         max_length=150,
#         unique=True,
#         blank=False,
#         null=False
#     )
#     email = models.EmailField(
#         verbose_name='Email',
#         max_length=254,
#         unique=True,
#         blank=False,
#         null=False
#     )
#     password = models.CharField(
#         verbose_name='Пароль',
#         max_length=150,
#         blank=False,
#         null=False
#     )

#     first_name = models.CharField(
#         verbose_name='Имя',
#         max_length=150,
#         blank=False,
#         null=False
#     )
#     last_name = models.CharField(
#         verbose_name='Фамилия',
#         max_length=150,
#         blank=False,
#         null=False
#     )

#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

#     def __str__(self):
#         return f'{self.username}, {self.email}'
