from rest_framework.permissions import BasePermission, SAFE_METHODS


class GuestPermission(BasePermission):
    allowed_methods = ("GET",)

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.method in self.allowed_methods
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class PartnerPermission(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and request.method in SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and obj.user == request.user


class AdminUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
