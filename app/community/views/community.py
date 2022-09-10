from rest_framework import mixins, viewsets

from community.models.community import Community
from community.serializers.community import CommunityModelSerializer


class CommunityViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Community.objects.all()
    serializer_class = CommunityModelSerializer

    def get_permissions(self):
        permissions = []
        return (permission() for permission in permissions)

