from rest_framework import serializers
from points.models.points import Points


class PointsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = (
            "id",
            "user",
            "start",
            "points"
        )


