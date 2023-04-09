from rest_framework.permissions import BasePermission

class IsWriteOnly(BasePermission):
    def has_permission(self, request, view):
        allowed_methods=['POST','PUT','PATCH','DELETE']
        if request.method in allowed_methods:
            return True
        else:
            False    