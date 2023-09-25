from django.urls import include, path
from rest_framework import routers

from api.views import (CategoriesViewSet, SalesViewSet,
                       ShopsViewSet, ForecastViewSet, UserViewSet)


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'sales', SalesViewSet, basename='sales')
router.register(r'shops', ShopsViewSet, basename='shops')
router.register(r'forecast', ForecastViewSet, basename='forecast')
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]
