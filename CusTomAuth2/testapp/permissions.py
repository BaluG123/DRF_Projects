from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsreadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False    

class IsSuper(BasePermission):
    def has_permission(self, request, view):
        username=request.user.username
        if username.lower() == 'venu':
            return True
        elif username != 0 and len(username)%2 ==0 and request.method in SAFE_METHODS:
            return True
        else:
            return False        
