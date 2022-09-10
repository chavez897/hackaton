from rest_framework import serializers
from courses.models.courses import Courses


class CoursesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            "id",
            "name",
            "description",
            "datetime",
            "instructor",
            "location",
            "picture",
            "delivery_mode",
        )


