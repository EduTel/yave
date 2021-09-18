from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import ClienteViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r"cliente", ClienteViewSet, basename='Cliente')


urlpatterns = [
    path("api/", include(router.urls)),
]