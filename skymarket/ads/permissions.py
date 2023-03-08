from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "It's not your business, homie"

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.author == user:
            return True
        return False
