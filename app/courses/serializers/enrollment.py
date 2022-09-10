from rest_framework import serializers
from courses.models.enrollment import Enrollment
from courses.serializers.courses import CoursesModelSerializer

class EnrollmentModelSerializer(serializers.ModelSerializer):
    course_info = CoursesModelSerializer(read_only=True, source='course')

    class Meta:
        model = Enrollment
        fields = (
            "id",
            "user",
            "start",
            "course",
            "status",
            "course_info"
        )
