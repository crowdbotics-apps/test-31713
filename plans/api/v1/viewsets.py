from rest_framework.viewsets import ModelViewSet
from plans.api.v1.serializers import PlanSerializer
# from users import permissions
from plans.models import Plan


class PlanViewSet(ModelViewSet):
    # permission_classes = [permissions.IsOwner,]
    serializer_class = PlanSerializer

    def get_queryset(self):
        queryset = Plan.objects.all()
        return queryset
