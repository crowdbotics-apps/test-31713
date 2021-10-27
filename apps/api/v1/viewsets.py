from rest_framework.viewsets import ModelViewSet
from apps.api.v1.serializers import AppSerializer
from users import permissions
from apps.models import App


class AppViewSet(ModelViewSet):
    permission_classes = [permissions.IsOwner,]
    serializer_class = AppSerializer

    def get_queryset(self):
        queryset = App.objects.filter(user=self.request.user)
        return queryset
