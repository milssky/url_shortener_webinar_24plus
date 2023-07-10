from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UrlViewSet

router_v1 = DefaultRouter()
router_v1.register("urls", UrlViewSet, basename="urls")


urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
