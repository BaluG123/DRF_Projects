from rest_framework.permissions import BasePermission,SAFE_METHODS

class CheckRead(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class CheckWrite(BasePermission):
    def has_permission(self, request, view):
        allowed_methods=['POST','PUT','PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False                    
