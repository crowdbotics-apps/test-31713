from rest_framework.viewsets import ModelViewSet
from subscriptions.api.v1.serializers import SubscriptionSerializer
# from users import permissions
from subscriptions.models import Subscription


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    
    http_method_names = ['get', 'post', "put", "patch", "head", 'options']
    
    # lookup_field = "app"
    def get_queryset(self):
        queryset = Subscription.objects.all()
        return queryset
