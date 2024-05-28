from rest_framework import permissions

class OnlyadminEdit(permissions.BasePermission):
    
# only admin can edit this page
    def has_permission(self, request, view):
          if request.method in permissions.SAFE_METHODS:
              return True
          else:
              return bool(request.user.is_staff )
        
    
# only the owner can edit this object or delete
class IsOwner(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
       
        # Instance must have an attribute named `user`.
        else:
            return obj.created_by == request.user or request.user.is_staff