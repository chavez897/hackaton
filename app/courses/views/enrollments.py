from rest_framework import mixins, viewsets

from courses.models.enrollment import Enrollment
from courses.serializers.enrollment import EnrollmentModelSerializer, CompleteCourseSerializer
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


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


    @action(detail=False, methods=["post"], url_path="complete")
    def payment_intent(self, request, *args, **kwargs):
        complete = CompleteCourseSerializer(data=request.data)
        complete.is_valid(raise_exception=True)
        return Response(
            complete.data,
            status=status.HTTP_200_OK,
        )