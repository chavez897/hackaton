from rest_framework import mixins, viewsets

from courses.models.courses import Courses
from courses.serializers.courses import CoursesModelSerializer


class CoursesViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Courses.objects.all()
    serializer_class = CoursesModelSerializer

    def get_permissions(self):
        permissions = []
        return (permission() for permission in permissions)

