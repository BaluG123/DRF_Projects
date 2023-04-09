from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsReadonly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False    

class IswriteOnly(BasePermission):
    def has_permission(self, request, view):
        allowed_methods=['POST','PUT','PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False                

class SuperCheck(BasePermission):
    def has_permission(self, request, view):
        username=request.user.username
        if username.lower() == "shukla":
            return True
        elif username != "" and len(username)%2 == 0 and request.method in SAFE_METHODS:
            return True
        else:
            return False         