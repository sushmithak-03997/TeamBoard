from rest_framework.permissions import BasePermission

from .models import Company


class IsAdminUser(BasePermission):
    """
    Grants access only to authenticated users whose linked Company
    has role == Company.Role.ADMIN. Deliberately does NOT use
    Django's is_staff / is_superuser flags.
    """

    message = 'Admin privileges are required to access this resource.'

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        company = getattr(user, 'company', None)
        if company is None:
            return False

        return company.role == Company.Role.ADMIN
