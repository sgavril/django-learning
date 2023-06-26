from django.core.exceptions import PermissionDenied
from django.http import HttpRequest

def check_sprinkle_rights(request: HttpRequest) -> HttpRequest:
    if request.user.can_sprinkle or request_.user.is_staff:
        # Python is dynamically typed ; can add attributes to request
        request.can_sprinkle
        return request

    raise PermissionDenied