from users.models import IpAddress
from extensions.utils import get_client_ip


class SaveIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        ip = get_client_ip(request)

        try:
            ip_address = IpAddress.objects.get(ip_address=ip)
        except IpAddress.DoesNotExist:
            ip_address = IpAddress.objects.create(
                ip_address=ip
            )

        request.user.ip_address = ip_address

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
