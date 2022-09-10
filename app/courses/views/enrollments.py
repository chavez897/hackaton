from rest_framework import mixins, viewsets

from courses.models.enrollment import Enrollment
from courses.serializers.enrollment import EnrollmentModelSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class EnrollmentsiewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,

):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentModelSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]

    filter_fields = ["user"]

    def get_permissions(self):
        permissions = []
        return (permission() for permission in permissions)

