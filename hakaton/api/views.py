from django_filters.rest_framework import DjangoFilterBackend
from products.models import Category, Forecast, Sale, Shop, Product, Store
from rest_framework import mixins, viewsets, filters
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from django.http import HttpResponse, StreamingHttpResponse
from rest_framework.response import Response
from rest_framework import permissions, status
import pandas as pd
import xlwt
from excel_response import ExcelResponse
from django.shortcuts import get_object_or_404

from .filter import CategoryFilter, ForecastFilter, SaleFilter, ShopFilter
from .pagination import LimitPageNumberPagination
from .permissions import IsAdminOrReadOnlyPermission
from .serializers import (
    CategorySerializer,
    ForecastGetSerializer,
    ForecastPostSerializer,
    SaleSerializer,
    ShopSerializer,
)


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
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


class ShopsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Shop.objects.all()
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    search_fields = (
        "^store",
    )
    serializer_class = ShopSerializer
    filterset_class = ShopFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)


class ForecastViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    # queryset = Forecast.objects.all()
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ForecastFilter
    search_fields = (
        "^store",
        "^sku",
    )
    permission_classes = (AllowAny,)

    def get_queryset(self):
        store = self.request.query_params.get('store')
        sku = self.request.query_params.get('sku')
        return Forecast.objects.filter(sku=sku, store=store)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ForecastGetSerializer
        return ForecastPostSerializer
    

    @action(
        methods=['GET'],
        detail=False,
        url_path='download_forecast_list',
        permission_classes=(AllowAny,),
    )
    def download_forecast_list(fact_sku, fact_store):
        sku = get_object_or_404(Category, sku=fact_sku)
        store = get_object_or_404(Shop, store=fact_store)
        data = Forecast.objects.filter(sku=sku, store=store)
        return ExcelResponse(data)

