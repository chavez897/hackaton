from rest_framework import serializers
from community.models.community import Community


class CommunityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = (
            "id",
            "name",
            "picture",
        )


