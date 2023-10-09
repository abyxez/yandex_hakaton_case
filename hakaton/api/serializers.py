from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.validators import UniqueValidator
from users.validators import validate_username
from datetime import datetime
from pprint import pprint

from django.db.models import F
from rest_framework import serializers

from users.models import User
from products.models import (
    Category,
    City,
    Division,
    Excel,
    Forecast,
    Format,
    Location,
    Product,
    ProductStore,
    Sale,
    ShoppingMall,
    Size,
    Store,
    Subcategory,
    Group,
)


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


class ShoppingMallSerializer(serializers.ModelSerializer):
    """Сериализатор для магазинов."""

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

    def to_representation(self, instance):
        return {
            "store": instance.store.hash_id,
            "city": instance.city,
            "division": instance.division,
            "format": instance.format,
            "location": instance.location,
            "size": instance.size,
            "is_active": instance.is_active,
        }


class ForecastSaleSerializer(serializers.ModelSerializer):
    """
    Для forecast, wape в SimpleSaleSerializer
    """

    forecast = serializers.SerializerMethodField()
    wape = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = (
            "forecast",
            "wape",
        )


class SimpleSaleSerializer(serializers.ModelSerializer):
    """
    Простой Сериализатор  для продаж  для просмотра.
    """

    forecast = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            "date",
            "sales_type",
            "sales_units",
            "sales_units_promo",
            "sales_rub",
            "sales_rub_promo",
            "forecast",
            "wape",
        )

    def get_forecast(self, obj):
        request = self.context.get("request")
        to_represent = []
        if request:
            dates = self.context.get("dates")
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            for date in dates:
                if Forecast.objects.filter(
                    sku=sku, store=store, date=date["date"]
                ).exists():
                    to_represent.append(
                        Forecast.objects.annotate(
                            forecast_units=F("sales_units"), forecast_dates=F("date")
                        )
                        .filter(sku=sku, store=store, forecast_dates=date["date"])
                        .values("forecast_units", "forecast_dates")
                    )
        return to_represent

    def to_representation(self, instance):
        wape, forecast_unit = None, None
        queryset = self.get_forecast(instance)
        forecast_dict = {}

        if queryset:
            for item in queryset:
                for _ in item:
                    forecast_dict[_["forecast_dates"]] = [_["forecast_units"]]

        if instance.date in forecast_dict.keys():
            forecast_unit = forecast_dict[instance.date]
            if forecast_unit is not None:
                wape = float(instance.sales_units / forecast_unit)

        return {
            "date": instance.date,
            "sales_type": instance.sales_type,
            "sales_units": instance.sales_units,
            "sales_units_promo": instance.sales_units_promo,
            "sales_rub": instance.sales_rub,
            "sales_rub_promo": instance.sales_rub_promo,
            "forecast": forecast_unit,
            "wape": wape,
        }


class SaleSerializer(serializers.ModelSerializer):
    """
    Сериализатор  для продаж .
    """

    store = serializers.StringRelatedField(read_only=True)
    sku = serializers.StringRelatedField(read_only=True)
    fact = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = ("store", "sku", "fact")

    def get_fact(self, obj):
        sales = Sale.objects.all()
        forecast = Forecast.objects.all()
        request = self.context.get("request")
        if request:
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            if sku and store:
                sales = sales.filter(store=store, sku=sku)
                dates = forecast.filter(store=store, sku=sku).values("date")
                serializer = SimpleSaleSerializer(
                    sales,
                    many=True,
                    read_only=True,
                    context={"request": request, "dates": dates},
                )
                return serializer.data
        serializer = SimpleSaleSerializer(sales, many=True, read_only=True)
        return serializer.data

    # def to_representation(self, instance):
    #     return {
    #         "store": instance.store.hash_id,
    #         "sku": instance.sku.hash_id,
    #         "fact": [{
    #             "date": instance.date,
    #             "sales_type": instance.sales_type,
    #             "sales_units": instance.sales_units,
    #             "sales_units_promo": instance.sales_units_promo,
    #             "sales_rub": instance.sales_rub,
    #             "sales_rub_promo": instance.sales_rub_promo,
    #             # 'forecast': instance.forecast,
    #             # 'wape': instance.wape,
    #     }],
    #     }


class SimpleUnitsPostSerializer(serializers.ModelSerializer):
    """
    Простой сериализатор количества для создания прогноза товара.
    """

    class Meta:
        model = Forecast
        fields = ("date", "sales_units")

    def to_representation(self, instance):
        return {f"{instance.date}": instance.sales_units}


class ProductStoreSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий товаров."""
    group = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    store = serializers.StringRelatedField()
    sku = serializers.StringRelatedField()
    forecast = serializers.SerializerMethodField()

    class Meta:
        model = ProductStore
        fields = (
            'store',
            "sku",
            "group",
            "category",
            "subcategory",
            "uom",
            "forecast",
        )

    # def to_representation(self, instance):
    #     return {
    #         'store': instance.store.hash_id,
    #         "sku": instance.sku.hash_id,
    #         "group": instance.group,
    #         "category": instance.category,
    #         "subcategory": instance.subcategory,
    #         "uom": instance.uom,
    #     }

    def get_group(self, obj):
        queryset = ProductStore.objects.all()
        request = self.context.get('request')
        if request:
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            if sku:
                queryset = queryset.filter(sku=sku)
                if store:
                    queryset = queryset.filter(store=store)
                    group = queryset.values('group')
                    return group
        else:
            return None
        return queryset

    def get_category(self, obj):
        queryset = ProductStore.objects.all()
        request = self.context.get('request')
        if request:
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            if sku:
                queryset = queryset.filter(sku=sku)
                if store:
                    queryset = queryset.filter(store=store)
                    group = queryset.values('category')
                    return group
        else:
            return None
        return queryset

    def get_subcategory(self, obj):
        queryset = ProductStore.objects.all()
        request = self.context.get('request')
        if request:
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            if sku:
                queryset = queryset.filter(sku=sku)
                if store:
                    queryset = queryset.filter(store=store)
                    group = queryset.filter(sku=sku).values('subcategory')
                    return group
        else:
            return None
        return queryset

    def get_forecast(self, obj):
        forecast = Forecast.objects.all()
        request = self.context.get("request")
        if request:
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            if sku:
                forecast = forecast.filter(sku=sku)
                if store:
                    forecast = forecast.filter(store=store)
        serializer = SimpleUnitsPostSerializer(forecast, many=True, read_only=True)
        return serializer.data




# class SimpleForecastPostSerializer(serializers.ModelSerializer):
#     """
#     Простой сериализатор товара для создания прогноза товара.
#     """

#     sales_units = SimpleUnitsPostSerializer(many=True)
#     sku = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Forecast
#         fields = ("sku", "sales_units")


class ForecastGetSerializer(serializers.ModelSerializer):
    """
    Cериализатор для просмотра прогноза товара.
    
    """

    store = StoreSerializer(read_only=True)
    sku = ProductSerializer(read_only=True)
    forecast = serializers.SerializerMethodField()
    # forecast = SimpleUnitsPostSerializer(read_only=True, source="*")
    # forecast = serializers.StringRelatedField(read_only=True)
    forecast_date = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = ("store", "sku", "forecast_date", "forecast")

    def get_forecast(self, obj):
        forecast = Forecast.objects.all()
        request = self.context.get("request")
        if request:
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            if sku and store:
                forecast = forecast.filter(store=store, sku=sku)
                serializer = SimpleUnitsPostSerializer(
                    forecast, many=True, read_only=True
                )
                return serializer.data
        serializer = SimpleUnitsPostSerializer(forecast, many=True, read_only=True)
        return serializer.data

    def get_forecast_date(self, obj):
        return datetime.today().strftime("%Y-%m-%d")

    def to_representation(self, instance):
        return {
            "store": instance.store.hash_id,
            "sku": instance.sku.hash_id,
            "forecast_date": self.get_forecast_date(instance),
            "forecast": {f"{instance.date}": instance.sales_units},
        }


class ForecastPostSerializer(serializers.ModelSerializer):
    """
    Cериализатор для создания прогноза товара.
    """

    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    sku = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    forecast = SimpleUnitsPostSerializer()
    forecast_date = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = ("store", "sku", "forecast_date", "forecast")

    def get_forecast_date(self, obj):
        return datetime.today().strftime("%Y-%m-%d")

    def create(self, validated_data):
        """Создание прогноза."""
        store = validated_data.pop("store")
        sku = validated_data.pop("sku")
        forecast_data = validated_data.pop("forecast")
        data = Forecast.objects.create(sku=sku, store=store, **forecast_data)
        data.save()
        return data

    def update(self, instance, validated_data):
        """Обновление прогноза."""
        Forecast.objects.filter(data=instance).delete()
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        request = self.context.get("request")
        return ForecastGetSerializer(instance, context={"request": request}).data


class UserListSerializer(UserSerializer):
    """Сериализатор для списка пользователей."""

    class Meta:
        model = User
        fields = ('email', 'id','username',
                  'first_name', 'last_name',
                  )


class UserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователей."""
    
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all()),
                    validate_username]
    )

    class Meta:
        model = User
        fields = (
            'id', 'email', 'username','first_name',
            'last_name', 'password'
        )


class ProductStoreForecastSerializer(serializers.ModelSerializer):
    """
    Сериализатор для категорий товаров и
    прогнозам продаж по датам.
    """

    store = serializers.SerializerMethodField()
    sku = serializers.StringRelatedField()
    forecast = serializers.SerializerMethodField()

    class Meta:
        model = ProductStore
        fields = (
            "store",
            "group",
            "category",
            "subcategory",
            "sku",
            "uom",
            "forecast",
        )

    def get_forecast(self, obj):
        forecast = Forecast.objects.all()
        request = self.context.get("request")
        if request:
            sku = request.query_params.get("sku")
            store = request.query_params.get("store")
            if sku and store:
                forecast = forecast.filter(store=store, sku=sku)
                serializer = SimpleUnitsPostSerializer(
                    forecast, many=True, read_only=True
                )
                return serializer.data
        serializer = SimpleUnitsPostSerializer(forecast, many=True, read_only=True)
        return serializer.data

    def get_store(self, obj):
        stores = Store.objects.all()
        request = self.context.get("request")
        if request:
            store = request.query_params.get("store")
            if store:
                shop = stores.filter(id=store)[0]
                serializer = StoreSerializer(shop, read_only=True)
                return serializer.data["hash_id"]
            else:
                return None
        serializer = StoreSerializer(stores, many=True, read_only=True)
        return serializer.data

    # def to_representation(self, instance):
    #     return {
    #         "store": instance.store.hash_id,
    #         "sku": instance.sku.hash_id,
    #         "group": instance.group,
    #         "forecast": {f"{instance.date}": instance.sales_units},
    #     }


class SaleForecastGetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для категорий товаров и
    прогнозам продаж по датам.
    """

    store = serializers.StringRelatedField(read_only=True)
    sku = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Excel
        fields = (
            "store",
            "category",
            "subcategory",
            "sku",
            "uom",
            "week",
            "sales_units",
            "target",
            "difference",
            "wape",
            "group",
        )

        def to_representation(self, instance):
            return {
                "store": instance.store.hash_id,
                "group": instance.group,
                "category": instance.category,
                "subcategory": instance.subcategory,
                "sku": instance.sku.hash_id,
                "uom": instance.uom,
                "week": instance.week,
                "sales_units": instance.sales_units,
                "target": instance.target,
                "difference": instance.difference,
                "wape": instance.wape,
            }
