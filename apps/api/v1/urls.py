from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.v1.viewsets import AppViewSet

app_name = "apps"

router = DefaultRouter()
router.register("", AppViewSet, basename="app")

urlpatterns = [
    path("", include(router.urls)),
]
