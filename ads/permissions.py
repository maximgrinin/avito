from rest_framework import permissions

from users.models import User


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'Updating this selection not allowed.'

    def has_object_permission(self, request, view, obj):
        return obj.owner_id == request.user.id


class AdUpdatePermission(permissions.BasePermission):
    message = 'Updating this ad not allowed.'

    def has_object_permission(self, request, view, obj):
        return obj.author_id == request.user.id or request.user.role in [User.ADMIN, User.MODERATOR]
