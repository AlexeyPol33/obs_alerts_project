from rest_framework import permissions
from .models import User, Configurations, Plugins


class isAccountOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: object):
        match obj:
            case User():
                return request.user == obj
            case Configurations():
                pass
            case Plugins():
                pass
            case _:
                raise


