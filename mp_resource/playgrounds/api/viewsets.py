from django.contrib.auth.models import Group
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from mp_resource.playgrounds.api.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
