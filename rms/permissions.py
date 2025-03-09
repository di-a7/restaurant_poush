from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.core.exceptions import PermissionDenied
class IsAuthenticatedOrReadOnly(BasePermission):
   def has_permission(self, request, view):
      return (request.method in SAFE_METHODS) or request.user and request.user.is_authenticated

class IsWaiterOrReadOnly(BasePermission):
   def has_permission(self, request, view):
      if request.method in SAFE_METHODS:
         return super().has_permission(request, view)
      user_group_exists = request.user.groups.filter(name='Waiter').exists()
      if not user_group_exists:
         raise PermissionDenied('You are not allowed to perform this action')
      return user_group_exists
