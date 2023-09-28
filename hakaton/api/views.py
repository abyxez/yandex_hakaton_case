from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,)

from products.models import (Sales, Shops, Categories, Forecast)

from .filter import SalesFilter, CategoriesFilter, ShopsFilter, ForecastFilter
from .pagination import LimitPageNumberPagination
from .permissions import IsAdminOrReadOnlyPermission
from .serializers import (CategoriesSerializer, SalesSerializer,
                          ShopsSerializer, ForecastGetSerializer,
                          ForecastPostSerializer)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = LimitPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoriesFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('^store', '^sku',)
    pagination_class = LimitPageNumberPagination
    filterset_class = SalesFilter
    permission_classes = (IsAdminOrReadOnlyPermission,)

    
  


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    pagination_class = LimitPageNumberPagination
    serializer_class = ShopsSerializer
    filterset_class = ShopsFilter
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
