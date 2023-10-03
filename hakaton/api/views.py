from django_filters.rest_framework import DjangoFilterBackend
from products.models import Category, Forecast, Sale, Shop
from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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
    serializer_class = ShopSerializer
    filterset_class = ShopFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)


class ForecastViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Forecast.objects.all()
    pagination_class = LimitPageNumberPagination
    filterset_class = ForecastFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ForecastGetSerializer
        return ForecastPostSerializer


# class UserViewSet(views.UserViewSet):
#     serializer_class = UserListSerializer
#     pagination_class = LimitPageNumberPagination
#     permission_classes = (IsAuthenticated,)
