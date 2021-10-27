from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subscriptions.api.v1.viewsets import SubscriptionViewSet

router = DefaultRouter()
router.register("", SubscriptionViewSet, basename="plans")

urlpatterns = [
    path("", include(router.urls)),
]
