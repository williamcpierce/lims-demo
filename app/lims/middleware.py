from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin


class HealthCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.META["PATH_INFO"] == "/ping/":
            return HttpResponse("pong!")


class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().partition(":")[0]
        if host == "www.williampierce.io":
            return HttpResponsePermanentRedirect(
                "https://williampierce.io" + request.path
            )
        else:
            return self.get_response(request)
