from django.http import HttpResponse
from oauth2_provider.views import ProtectedResourceView


class ApiEndpoint(ProtectedResourceView):
    """Example of class-based view by backend render the HTML document"""
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World2")
