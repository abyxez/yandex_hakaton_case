from django.db.models import CharField, SlugField, ForeignKey, Model, CASCADE, FloatField, PositiveIntegerField, IntegerField, DateField
# from django.contrib.auth.models import AbstractUser


class Product(Model):
    name = CharField(
        'Название продукта',
        unique=True,
        max_length=200,
    )


class Shop(Model):
    """Модель магазинов"""
    store = CharField(verbose_name='Название магазина',
                             max_length=200, unique=True)
    city = CharField(verbose_name='Город', max_length=200)
    divizion = CharField(verbose_name='Дивизион', max_length=200)
    format = SlugField(verbose_name='Формат магазина',
                              max_length=200)
    loc = SlugField(verbose_name='Локация магазина',
                           max_length=200)
    size = SlugField(verbose_name='Тип размера магазина',
                            max_length=200)
    is_active = CharField(
        verbose_name='Флаг активного магазина', max_length=200)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.store


class Category(Model):
    """Модель категорий"""
    sku = CharField(
        'Наименование товара ',
        max_length=200,
    )
    group = CharField(verbose_name='Группа товара ',
                             max_length=200)
    category = CharField(verbose_name='Категория товара',
                                max_length=200)
    subcategory = CharField(verbose_name='Подкатегория товара',
                                   max_length=200)
    uom = SlugField(
        verbose_name='Маркер товара -на вес или шт')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.sku


class Sale(Model):
    """Модель продаж"""
    store = CharField(
        # Shop, on_delete=CASCADE,
        # related_name='sales',
        verbose_name='магазин',
        max_length=200,
    )
    sku = CharField(
        verbose_name='товар',
        max_length=200,
    )

    date = DateField(verbose_name='Дата продажи товара', blank=True, null=True)
    sales_type = PositiveIntegerField(verbose_name='Флаг наличия промо')
    sales_units = FloatField(
        verbose_name='Число проданных товаров без признака промо')
    sales_units_promo = FloatField(
        verbose_name='Число проданных товаров c признаком промо')
    sales_rub = FloatField(
        verbose_name='Цена проданных товаров без признака промо')
    sales_rub_promo = FloatField(
        verbose_name='Цена проданных товаров c признаком промо')

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return (f'{self.date} {self.sales_type}'
                f'{self.sales_units} {self.sales_units_promo}'
                f'{self.sales_rub} {self.sales_rub_promo}')


class Forecast(Model):
    """Модель прогноза продаж."""

    store = CharField(
        # Shop, on_delete=CASCADE,
        # related_name='forecast',
        verbose_name='магазин',
        max_length=200,
    )
    sku = CharField(
        # Product, on_delete=CASCADE,
        # related_name='forecast',
        verbose_name='товар',
        max_length=200,
    )
    # forecast_date = DateField(verbose_name='Дата отчета')
    date = DateField(verbose_name='Дата прогноза продажи')
    sales_units = PositiveIntegerField(
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
#     username = CharField(
#         verbose_name='Имя пользователя',
#         validators=(validate_username,),
#         max_length=150,
#         unique=True,
#         blank=False,
#         null=False
#     )
#     email = EmailField(
#         verbose_name='Email',
#         max_length=254,
#         unique=True,
#         blank=False,
#         null=False
#     )
#     password = CharField(
#         verbose_name='Пароль',
#         max_length=150,
#         blank=False,
#         null=False
#     )

#     first_name = CharField(
#         verbose_name='Имя',
#         max_length=150,
#         blank=False,
#         null=False
#     )
#     last_name = CharField(
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
