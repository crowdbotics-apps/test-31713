from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):

        # Only the owner can performany action
        return obj.user == request.user