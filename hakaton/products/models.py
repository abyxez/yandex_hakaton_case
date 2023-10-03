from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    FloatField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    Model,
    PositiveIntegerField,
    SlugField,
)

# from django.contrib.auth.models import AbstractUser


class Product(Model):
    """
    Вспомогательная модель: из hash_id в id для товаров.
    """

    name = CharField(
        "Название товара",
        max_length=200,
        blank=True,
        null=True,
    )
    hash_id = CharField(
        "Хэшированный ID",
        unique=True,
        max_length=100,
    )


class Store(Model):
    """
    Вспомогательная модель: из hash_id в id для магазинов.
    """

    name = CharField(
        "Название магазина",
        max_length=200,
        blank=True,
        null=True,
        default="Лента",
    )
    hash_id = CharField(
        "Хэшированный ID",
        unique=True,
        max_length=100,
    )


class Shop(models.Model):
    """Модель магазинов"""

    store = ForeignKey(
        verbose_name="Магазин",
        to=Store,
        related_name="shops",
        on_delete=CASCADE,
    )
    city = CharField(
        "Город",
        max_length=200,
    )
    divizion = CharField(
        "Дивизион",
        max_length=200,
    )
    format = IntegerField(
        verbose_name="Формат магазина",
    )
    loc = IntegerField(
        verbose_name="Локация магазина",
    )
    size = IntegerField(
        verbose_name="Тип размера магазина",
    )
    is_active = IntegerField(
        verbose_name="Флаг активного магазина",
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.store


# class ProductShop(Model):
#     store = ForeignKey(
#         to=Shop,
#         on_delete=CASCADE,
#         verbose_name=''
#     )
#     product = ForeignKey(
#         to=Product,
#         on_delete=CASCADE,
#         verbose_name=''
#     )


class Category(Model):
    """Модель категорий"""

    sku = ForeignKey(
        to=Product,
        verbose_name="Наименование товара ",
        max_length=200,
        on_delete=CASCADE,
    )
    group = CharField(verbose_name="Группа товара ", max_length=200)
    category = CharField(verbose_name="Категория товара", max_length=200)
    subcategory = CharField(verbose_name="Подкатегория товара", max_length=200)
    uom = IntegerField(verbose_name="Маркер товара -на вес или шт")

    class Meta:
        ordering = ("id",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.sku


class Sale(models.Model):
    """Модель продаж"""

    store = ForeignKey(
        to=Store,
        on_delete=CASCADE,
        related_name="sales",
        verbose_name="магазин",
    )
    sku = ForeignKey(
        to=Product,
        verbose_name="товар",
        on_delete=CASCADE,
        related_name="sales",
    )

    date = DateField(verbose_name="Дата продажи товара", blank=True, null=True)
    sales_type = PositiveIntegerField(verbose_name="Флаг наличия промо")
    sales_units = FloatField(verbose_name="Число проданных товаров без признака промо")
    sales_units_promo = FloatField(
        verbose_name="Число проданных товаров c признаком промо"
    )
    sales_rub = FloatField(verbose_name="Цена проданных товаров без признака промо")
    sales_rub_promo = FloatField(
        verbose_name="Цена проданных товаров c признаком промо"
    )

    class Meta:
        ordering = ("-date",)
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return (
            f"{self.date} {self.sales_type}"
            f"{self.sales_units} {self.sales_units_promo}"
            f"{self.sales_rub} {self.sales_rub_promo}"
        )


class Forecast(models.Model):
    """Модель прогноза продаж."""

    store = ForeignKey(
        to=Store,
        on_delete=CASCADE,
        related_name="forecasts",
        verbose_name="магазин",
    )
    sku = ForeignKey(
        Product,
        on_delete=CASCADE,
        related_name="forecast",
        verbose_name="товар",
    )
    # forecast_date = DateField(verbose_name='Дата отчета')
    date = DateField(verbose_name="Дата прогноза продажи")
    sales_units = PositiveIntegerField(
        verbose_name="Прогнозируемый спрос в шт",
    )

    class Meta:
        ordering = ("date",)
        verbose_name = "Прогноз продаж"
        verbose_name_plural = "Прогноз продаж"

    def __str__(self):
        return f"{self.date}:{self.sales_units}"


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
