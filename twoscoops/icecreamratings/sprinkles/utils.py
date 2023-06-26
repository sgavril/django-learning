from django.core.exceptions import PermissionDenied
from django.http import HttpRequest

def check_sprinkle_rights(request: HttpRequest) -> HttpRequest:
    if request.user.can_sprinkle or request_.user.is_staff:
        return request

    raise PermissionDenied