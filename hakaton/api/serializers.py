# from djoser.serializers import UserCreateSerializer, UserSerializer
# from rest_framework.validators import UniqueValidator
# from products.validators import validate_username
from datetime import datetime

from products.models import Category, Forecast, Product, Sale, Shop, Store
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = (
            "id",
            "name",
        )


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = (
            "id",
            "name",
        )


class ShopSerializer(serializers.ModelSerializer):
    """Сериализатор для магазинов."""

    class Meta:
        model = Shop
        fields = (
            "store",
            "city",
            "divizion",
            "format",
            "loc",
            "size",
            "is_active",
        )

    def to_representation(self, instance):
        return {
            "store": instance.store.hash_id,
            "city": instance.city,
            "divizion": instance.divizion,
            "format": instance.format,
            "loc": instance.loc,
            "size": instance.size,
            "is_active": instance.is_active,
        }


class SimpleSaleSerializer(serializers.ModelSerializer):
    """
    Простой Сериализатор  для продаж  для просмотра.
    """

    class Meta:
        model = Sale
        fields = (
            "date",
            "sales_type",
            "sales_units",
            "sales_units_promo",
            "sales_rub",
            "sales_rub_promo",
        )


class SaleSerializer(serializers.ModelSerializer):
    """
    Сериализатор  для продаж .
    """

    store = StoreSerializer(read_only=True)
    sku = ProductSerializer(read_only=True)
    fact = SimpleSaleSerializer(read_only=True, source="*")
 

    class Meta:
        model = Sale
        fields = ("store", "sku", "fact")

    def to_representation(self, instance):
        return {
            "store": instance.store.hash_id,
            "sku": instance.sku.hash_id,
            "fact": [{
                "date": instance.date,
                "sales_type": instance.sales_type,
                "sales_units": instance.sales_units,
                "sales_units_promo": instance.sales_units_promo,
                "sales_rub": instance.sales_rub,
                "sales_rub_promo": instance.sales_rub_promo,
        }],
        }


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий товаров."""
    

    class Meta:
        model = Category
        fields = (
            "sku",
            "group",
            "category",
            "subcategory",
            "uom",
        )

    def to_representation(self, instance):
        return {
            "sku": instance.sku.hash_id,
            "group": instance.group,
            "category": instance.category,
            "subcategory": instance.subcategory,
            "uom": instance.uom,
        }


class SimpleUnitsPostSerializer(serializers.ModelSerializer):
    """
    Простой сериализатор количества для создания прогноза товара.
    """

    class Meta:
        model = Forecast
        fields = ("date", "sales_units")

    


class SimpleForecastPostSerializer(serializers.ModelSerializer):
    """
    Простой сериализатор товара для создания прогноза товара.
    """

    sales_units = SimpleUnitsPostSerializer(many=True)
    sku = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = ("sku", "sales_units")


class ForecastGetSerializer(serializers.ModelSerializer):
    """
    Cериализатор для просмотра прогноза товара.
    """

    store = serializers.StringRelatedField(read_only=True)
    sku = serializers.StringRelatedField(read_only=True)
    forecast = SimpleUnitsPostSerializer(many=True, read_only=True)
    forecast_date = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = ("store", "sku", "forecast_date", "forecast")

    def get_forecast_date(self, obj):
        return datetime.today().strftime("%Y-%m-%d")
    
    def to_representation(self, instance):
        return {
            "store": instance.store.hash_id,
            "forecast_date": datetime.today().strftime("%Y-%m-%d"),
            "forecast": {
                    "sku": instance.sku.hash_id,
                    "sales_units": {
                        str(instance.date) : instance.sales_units
                    },
                },
        }


class ForecastPostSerializer(serializers.ModelSerializer):
    """
    Cериализатор для создания прогноза товара.
    """

    store = serializers.StringRelatedField(read_only=True)
    forecast = SimpleForecastPostSerializer(many=True)
    forecast_date = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ("store", "forecast_date", "forecast")

    def get_forecast_date(self, obj):
        return datetime.today().strftime("%Y-%m-%d")

    def create(self, validated_data):
        """Создание прогноза."""
        store = validated_data.pop("store")
        sku = validated_data.pop("sku")
        date = validated_data.pop("date")
        sales_units = validated_data.pop("sales_units")
        data = SimpleUnitsPostSerializer()
        # forecast_date = validated_data.pop("forecast_date")
        data = Forecast.objects.create(
            sku=sku,
            store=store,
            date=date,
            forecast_date=datetime.today().strftime("%Y-%m-%d"),
            sales_units=sales_units,
            **validated_data
        )
        data.save()
        return data

    def update(self, instance, validated_data):
        """Обновление прогноза."""
        Forecast.objects.filter(data=instance).delete()
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        request = self.context.get("request")
        return ForecastGetSerializer(instance, context={"request": request}).data


# class UserListSerializer(UserSerializer):
#     """Сериализатор для списка пользователей."""

#     class Meta:
#         model = User
#         fields = ('email', 'id', 'username',
#                   'first_name', 'last_name',
#                   )


# class UserCreateSerializer(UserCreateSerializer):
#     """Сериализатор для создания пользователей."""
#     username = serializers.CharField(
#         validators=[UniqueValidator(queryset=User.objects.all()),
#                     validate_username]
#     )
#     email = serializers.EmailField(
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )

#     class Meta:
#         model = User
#         fields = (
#             'id', 'email', 'username', 'first_name',
#             'last_name', 'password'
#         )
