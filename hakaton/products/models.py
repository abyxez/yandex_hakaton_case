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
    Модель товара.
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

    def __str__(self):
        return self.hash_id


class Store(Model):
    """
    Модель магазина.
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

    def __str__(self):
        return self.hash_id


class Category(Model):
    """
    Модель категорий.
    """

    name = CharField(
        "Название категории",
        max_length=200,
        unique=True,
        blank=True,
        null=True,
    )
    hash_id = CharField(
        "Хэшированный ID",
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.hash_id


class Subcategory(Model):
    """
    Модель подкатегорий.
    """

    name = CharField(
        "Название подкатегории",
        max_length=200,
        unique=True,
        blank=True,
        null=True,
    )
    hash_id = CharField(
        "Хэшированный ID",
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.hash_id


class Group(Model):
    """
    Модель групп.
    """

    name = CharField(
        "Название группы",
        max_length=200,
        unique=True,
        blank=True,
        null=True,
    )
    hash_id = CharField(
        "Хэшированный ID",
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.hash_id


class City(Model):
    """
    Модель города.
    """

    name = CharField(
        "Название города",
        max_length=200,
        unique=True,
        blank=True,
        null=True,
    )
    hash_id = CharField(
        "Хэшированный ID",
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.hash_id


class Division(Model):
    """
    Модель дивизиона.
    """

    name = CharField(
        "Название дивизиона",
        max_length=200,
        unique=True,
        blank=True,
        null=True,
    )
    hash_id = CharField(
        "Хэшированный ID",
        unique=True,
        max_length=100,
    )

    def __str__(self):
        return self.hash_id


class Format(Model):
    """
    Модель формата.
    """

    name = CharField(
        "Название формата",
        max_length=200,
        unique=True,
    )

    def __str__(self):
        return self.name


class Location(Model):
    """
    Модель локации.
    """

    name = CharField(
        "Название локации",
        max_length=200,
        unique=True,
    )

    def __str__(self):
        return self.name


class Size(Model):
    """
    Модель размера магазина.
    """

    name = CharField(
        "Размерная характеристика",
        max_length=200,
        unique=True,
    )

    def __str__(self):
        return self.name


class ShoppingMall(Model):
    """Модель торгового центра."""

    store = ForeignKey(
        verbose_name="Магазин",
        to=Store,
        related_name="shops",
        on_delete=CASCADE,
    )
    city = ForeignKey(
        to=City,
        verbose_name="Город",
        related_name="shops",
        max_length=200,
        on_delete=CASCADE,
    )
    division = ForeignKey(
        to=Division,
        verbose_name="Дивизион",
        related_name="shops",
        max_length=200,
        on_delete=CASCADE,
    )
    format = ForeignKey(
        to=Format,
        verbose_name="Формат",
        related_name="shops",
        max_length=200,
        on_delete=CASCADE,
    )
    location = ForeignKey(
        to=Location,
        verbose_name="Локация",
        max_length=200,
        on_delete=CASCADE,
    )
    size = ForeignKey(
        to=Size,
        verbose_name="Размер",
        related_name="shops",
        max_length=200,
        on_delete=CASCADE,
    )
    is_active = IntegerField(
        verbose_name="Флаг активного магазина",
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return (
            f"{self.store} {self.city} {self.division} "
            f"{self.format} {self.location} {self.size} {self.is_active}"
        )


class ProductStore(Model):
    """Модель категорий и товаров в магазине."""

    store = ForeignKey(
        to=Store,
        on_delete=CASCADE,
        related_name="product_store",
        verbose_name="Торговый центр",
    )
    sku = ForeignKey(
        to=Product,
        verbose_name="Наименование товара",
        max_length=200,
        related_name="product_store",
        on_delete=CASCADE,
    )
    group = ForeignKey(
        to=Group,
        verbose_name="Товарная группа",
        max_length=200,
        related_name="product_store",
        on_delete=CASCADE,
    )
    category = ForeignKey(
        to=Category,
        verbose_name="Категория",
        max_length=200,
        related_name="product_store",
        on_delete=CASCADE,
    )
    subcategory = ForeignKey(
        to=Subcategory,
        verbose_name="Подкатегория",
        max_length=200,
        related_name="product_store",
        on_delete=CASCADE,
    )
    uom = IntegerField(verbose_name="Маркер развесовки: в Кг или Шт")

    class Meta:
        ordering = ("id",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return (
            f"{self.sku} {self.group} {self.category} " f"{self.subcategory} {self.uom}"
        )


class Sale(Model):
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
            f"{self.date} {self.sales_type} "
            f"{self.sales_units} {self.sales_units_promo} "
            f"{self.sales_rub} {self.sales_rub_promo}"
        )


class Forecast(Model):
    """Модель прогноза продаж."""

    store = ForeignKey(
        to=Store,
        on_delete=CASCADE,
        related_name="forecast",
        verbose_name="магазин",
    )
    sku = ForeignKey(
        Product,
        on_delete=CASCADE,
        related_name="forecast",
        verbose_name="товар",
    )
    date = DateField(verbose_name="Дата прогноза продажи")
    sales_units = PositiveIntegerField(
        verbose_name="Прогнозируемый спрос в шт",
    )

    class Meta:
        ordering = ("date",)
        verbose_name = "Прогноз продаж"
        verbose_name_plural = "Прогноз продаж"

    def __str__(self):
        return f"{self.store} {self.sku} {self.date} {self.sales_units}"


class Excel(Model):
    """
    Для вывода в эксель
    """

    store = ForeignKey(
        to=Store,
        on_delete=CASCADE,
        related_name="excel",
        verbose_name="Торговый центр",
    )
    sku = ForeignKey(
        to=Product,
        verbose_name="Наименование товара",
        max_length=200,
        related_name="excel",
        on_delete=CASCADE,
    )
    group = ForeignKey(
        to=Group,
        verbose_name="Товарная группа",
        max_length=200,
        related_name="excel",
        on_delete=CASCADE,
    )
    category = ForeignKey(
        to=Category,
        verbose_name="Категория",
        max_length=200,
        related_name="excel",
        on_delete=CASCADE,
    )
    subcategory = ForeignKey(
        to=Subcategory,
        verbose_name="Подкатегория",
        max_length=200,
        related_name="excel",
        on_delete=CASCADE,
    )
    uom = IntegerField(verbose_name="Маркер развесовки: в Кг или Шт")
    week = IntegerField()
    sales_units = FloatField(
        verbose_name="Число проданных товаров без признака промо",
        null=True,
        blank=False,
    )
    target = FloatField(null=True, blank=False)
    difference = FloatField(null=True, blank=False)
    wape = FloatField(null=True, blank=False)

    class Meta:
        ordering = ("week",)
        verbose_name = "Вывод статистики"
        verbose_name_plural = "Вывод статистики"

    def __str__(self):
        return (
            f"{self.store} {self.sku} "
            f"{self.group} {self.category} {self.subcategory }"
            f"{self.uom} {self.week} {self.sales_units}"
            f"{self.target} {self.difference} {self.wape}"
        )

