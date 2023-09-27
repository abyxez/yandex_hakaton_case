from rest_framework import serializers
from products.models import (Categories, Shops, Sales, Forecast)
# from djoser.serializers import UserCreateSerializer, UserSerializer
# from rest_framework.validators import UniqueValidator
# from products.validators import validate_username


class ShopsSerializer(serializers.ModelSerializer):
    """Сериализатор для магазинов."""

    class Meta:
        model = Shops
        fields = '__all__'


class SimpleSalesSerializer(serializers.ModelSerializer):
    """
    Простой Сериализатор  для продаж  для просмотра.
    """

    class Meta:
        model = Sales
        fields = ('date', 'sales_type', 'sales_units',
                  'sales_units_promo', 'sales_rub', 'sales_run_promo')


class SalesSerializer(serializers.ModelSerializer):
    """
    Сериализатор  для продаж .
    """
    store = serializers.StringRelatedField(read_only=True)
    sku = serializers.StringRelatedField(read_only=True)
    fact = SimpleSalesSerializer(many=True, read_only=True)

    class Meta:
        model = Sales
        fields = ('id', 'store', 'sku', 'fact')


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий товаров."""

    class Meta:
        model = Categories
        fields = '__all__'


class SimpleUnitsPostSerializer(serializers.ModelSerializer):
    """
    Простой сериализатор количества для создания прогноза товара.
    """

    class Meta:
        model = Forecast
        fields = ('date', 'sales_units')


class SimpleForecastPostSerializer(serializers.ModelSerializer):
    """
    Простой сериализатор товара для создания прогноза товара.
    """
    sales_units = SimpleUnitsPostSerializer(many=True, read_only=True)
    sku = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Forecast
        fields = ('sku', 'sales_units')


class ForecastGetSerializer(serializers.ModelSerializer):
    """
    Cериализатор для просмотра прогноза товара.
    """
    store = serializers.StringRelatedField(read_only=True)
    sku = serializers.StringRelatedField(read_only=True)
    forecast = SimpleUnitsPostSerializer(many=True, read_only=True)

    class Meta:
        model = Forecast
        fields = ('store', 'sku', 'forecast_date', 'forecast')


class ForecastPostSerializer(serializers.ModelSerializer):
    """
    Cериализатор для создания прогноза товара.
    """
    store = serializers.StringRelatedField(read_only=True)
    forecast = SimpleForecastPostSerializer(many=True)
    forecast_date = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Forecast
        fields = ('store', 'forecast_date', 'forecast')

    def create(self, validated_data):
        """Создание прогноза."""
        store = validated_data.pop('store')
        forecast = validated_data.pop('forecast')
        forecast_date = validated_data.pop('forecast_date')
        data = Forecast.objects.create(store=store, forecast=forecast,
                                       forecast_date=forecast_date,
                                       **validated_data)
        data.save()
        return data

    def update(self, instance, validated_data):
        """Обновление прогноза."""
        Forecast.objects.filter(data=instance).delete()
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        return ForecastGetSerializer(
            instance,
            context={'request': request}
        ).data

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