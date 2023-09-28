from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,)

from products.models import (Sale, Shop, Category, Forecast)

from .filter import SaleFilter, CategoryFilter, ShopFilter, ForecastFilter
from .pagination import LimitPageNumberPagination
from .permissions import IsAdminOrReadOnlyPermission
from .serializers import (CategorySerializer, SaleSerializer,
                          ShopSerializer, ForecastGetSerializer,
                          ForecastPostSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('^store', '^sku',)
    pagination_class = LimitPageNumberPagination
    filterset_class = SaleFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    pagination_class = LimitPageNumberPagination
    serializer_class = ShopSerializer
    filterset_class = ShopFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    pagination_class = LimitPageNumberPagination
    filterset_class = ForecastFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ForecastGetSerializer
        return ForecastPostSerializer
    
# class UserViewSet(views.UserViewSet):
#     serializer_class = UserListSerializer
#     pagination_class = LimitPageNumberPagination
#     permission_classes = (IsAuthenticated,)
