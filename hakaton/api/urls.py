from django.urls import include, path
from rest_framework import routers

from api.views import (
    ProductStoreViewSet,
    ForecastViewSet,
    SaleViewSet,
    ShopsViewSet,
    StatisticSaleForecastViewSet,
    StatisticViewSet,
)

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products_store", ProductStoreViewSet, basename="categories")
router.register(r"sales", SaleViewSet, basename="sales")
router.register(r"shops", ShopsViewSet, basename="shops")
router.register(r"forecast", ForecastViewSet, basename="forecast")
# router.register(r'users', UserViewSet, basename='users')
router.register(r"statistics", StatisticViewSet, basename="statistics")
router.register(
    r"statistics_extended", StatisticSaleForecastViewSet, basename="statistics_2"
)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
