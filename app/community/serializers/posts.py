from rest_framework import serializers
from community.models.posts import Posts


class PostsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = (
            "id",
            "community",
            "post",
        )


