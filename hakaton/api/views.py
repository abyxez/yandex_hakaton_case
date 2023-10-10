from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from excel_response import ExcelResponse
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from djoser import views

from users.models import User
from products.models import (
    Category,
    Excel,
    Forecast,
    ProductStore,
    Sale,
    ShoppingMall,
)

from .filter import CategoryFilter, ForecastFilter, SaleFilter, ShopFilter
from .pagination import LimitPageNumberPagination
from .permissions import IsAdminOrReadOnlyPermission
from .serializers import (
    ForecastGetSerializer,
    ForecastPostSerializer,
    ProductStoreSerializer,
    SaleForecastGetSerializer,
    SaleSerializer,
    ShoppingMallSerializer,
    UserListSerializer,UserCreateSerializer
)


class ProductStoreViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ProductStore.objects.all()
    serializer_class = ProductStoreSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
    search_fields = ("^sku",)
    permission_classes = (IsAdminOrReadOnlyPermission,)


class SaleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = (
        "^store",
        "^sku",
    )
    pagination_class = LimitPageNumberPagination
    filterset_class = SaleFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)

    def get_queryset(self):
        queryset = self.queryset
        store = self.request.query_params.get("store")
        if store:
            queryset = queryset.filter(store=store)
        sku = self.request.query_params.get("sku")
        if sku:
            queryset = queryset.filter(sku=sku)
        return queryset


class ShopsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ShoppingMall.objects.all()
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    search_fields = ("^store",)
    serializer_class = ShoppingMallSerializer
    filterset_class = ShopFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)


class ForecastViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Forecast.objects.all()
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ForecastFilter
    search_fields = (
        "^store",
        "^sku",
    )
    permission_classes = (IsAdminOrReadOnlyPermission,)

    def get_queryset(self):
        queryset = self.queryset
        store = self.request.query_params.get("store")
        if store:
            queryset = queryset.filter(store=store)
        sku = self.request.query_params.get("sku")
        if sku:
            queryset = queryset.filter(sku=sku)
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ForecastGetSerializer
        return ForecastPostSerializer

    @action(
        methods=["GET"],
        detail=False,
        url_path="download_forecast_list",
        permission_classes=(IsAuthenticatedOrReadOnly,)
    )

    def download_forecast_list(fact_sku, fact_store):
        sku = get_object_or_404(Category, sku=fact_sku)
        store = get_object_or_404(ShoppingMall, store=fact_store)
        data = Forecast.objects.filter(sku=sku, store=store)
        return ExcelResponse(data)


class StatisticSaleForecastViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Excel.objects.all()
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    search_fields = (
        "^store",
        "^sku",
    )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SaleForecastGetSerializer


class StatisticViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ProductStore.objects.all()
    serializer_class = ProductStoreSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
    search_fields = ("^sku",)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = self.queryset
        store = self.request.query_params.get("store")
        if store:
            queryset = queryset.filter(store=store)

        sku = self.request.query_params.get("sku")
        if sku:
            queryset = queryset.filter(sku=sku)

        return queryset
    

class UserViewSet(views.UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = LimitPageNumberPagination
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']

