from rest_framework import mixins, viewsets

from points.models.points import Points
from points.serializers.points import PointsModelSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class PointsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Points.objects.all()
    serializer_class = PointsModelSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]

    filter_fields = ["user"]

    def get_permissions(self):
        permissions = []
        return (permission() for permission in permissions)

