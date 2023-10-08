from api.views import CategoryViewSet, ForecastViewSet, SaleViewSet, ShopsViewSet, UserViewSet
from django.urls import include, path
from rest_framework import routers

app_name = "api"

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"sales", SaleViewSet, basename="sales")
router.register(r"shops", ShopsViewSet, basename="shops")
router.register(r"forecast", ForecastViewSet, basename="forecast")
# router.register(r'download', )
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
