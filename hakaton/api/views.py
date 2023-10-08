from django_filters.rest_framework import DjangoFilterBackend
from products.models import Category, Forecast, Sale, Shop, Product, Store, Excel
from users.models import User
from rest_framework import mixins, viewsets, filters
from rest_framework.generics import GenericAPIView, ListAPIView
from djoser import views

from rest_framework.decorators import action
# from django.http import HttpResponse, StreamingHttpResponse
# from rest_framework.response import Response
# from rest_framework import permissions, status
# import pandas as pd
# import xlwt
from excel_response import ExcelResponse
from django.shortcuts import get_object_or_404

from .filter import CategoryFilter, ForecastFilter, SaleFilter, ShopFilter, SaleForecastFilter
from .pagination import LimitPageNumberPagination
from .permissions import IsAdminOrReadOnlyPermission
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)

from .serializers import (CategorySerializer, ForecastGetSerializer,
                          ForecastPostSerializer, SaleSerializer,
                          ShopSerializer, UserListSerializer, SaleForecastGetSerializer)


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

    def get_queryset(self):
        queryset = self.queryset
        store = self.request.query_params.get('store')
        if store:
            queryset = queryset.filter(store=store)
        sku = self.request.query_params.get('sku')
        if sku:
            queryset = queryset.filter(sku=sku)
        return queryset


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
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.DestroyModelMixin
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

    # def get_queryset(self):
    #     store = self.request.query_params.get('store')
    #     sku = self.request.query_params.get('sku')
    #     return Forecast.objects.filter(sku=sku, store=store)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ForecastGetSerializer
        return ForecastPostSerializer

    @action(
        methods=['GET'],
        detail=False,
        url_path='download_forecast_list',
        permission_classes=(IsAuthenticatedOrReadOnly,),
    )
    def download_forecast_list(fact_sku, fact_store):
        sku = get_object_or_404(Category, sku=fact_sku)
        store = get_object_or_404(Shop, store=fact_store)
        data = Forecast.objects.filter(sku=sku, store=store)
        return ExcelResponse(data)
    
class Statistic2ViewSet(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Excel.objects.all()
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SaleForecastFilter
    search_fields = (
        "^store",
        "^sku",
    )
    permission_classes = (IsAdminOrReadOnlyPermission,)
    serializer_class = SaleForecastGetSerializer

    # def get_queryset(self):
    #     store = self.request.query_params.get('store')
    #     sku = self.request.query_params.get('sku')
    #     return Forecast.objects.filter(sku=sku, store=store)


    @action(
        methods=['GET'],
        detail=False,
        url_path='statistic_2',
        permission_classes=(IsAuthenticatedOrReadOnly,),
    )
    def statistic_2(fact_sku, fact_store):
        sku = get_object_or_404(Category, sku=fact_sku)
        store = get_object_or_404(Shop, store=fact_store)
        data = Excel.objects.filter(sku=sku, store=store)
        return ExcelResponse(data)
    

class UserViewSet(views.UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = LimitPageNumberPagination
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']
