from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models.schools import Schools
from users.serializers.schools import SchoolsModelSerializer


class SchoolsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Schools.objects.all()
    serializer_class = SchoolsModelSerializer

    def create(self, request, *args, **kwargs):
        if Schools.objects.filter(name=request.data["name"]).exists():
            return Response({}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        permissions = []
        return (permission() for permission in permissions)
