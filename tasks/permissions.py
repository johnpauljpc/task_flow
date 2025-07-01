from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOfTask(BasePermission):
    """
    Custom permission to only allow owners of a task to view/edit/delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS → read-only access
        if request.method in SAFE_METHODS:
            return obj.owner == request.user

        # For PUT, PATCH, DELETE → ensure user is the owner
        return obj.owner == request.user
