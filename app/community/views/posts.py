from rest_framework import mixins, viewsets

from community.models.posts import Posts
from community.serializers.posts import PostsModelSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class PostViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Posts.objects.all()
    serializer_class = PostsModelSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]

    filter_fields = ["community"]

    def get_permissions(self):
        permissions = []
        return (permission() for permission in permissions)

