from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsWrite(BasePermission):
    def has_permission(self, request, view):
        allowed_methods=['POST','PATCH','PUT']
        if request.method in allowed_methods:
            return True
        else:
            return False    
        