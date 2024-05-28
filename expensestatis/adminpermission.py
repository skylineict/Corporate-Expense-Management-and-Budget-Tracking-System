from rest_framework.permissions import BasePermission

class Adminonly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and  request.user.is_staff)