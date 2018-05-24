from oauth2_provider.views import ProtectedResourceView
from rest_framework.response import Response


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return Response("Hello World")
