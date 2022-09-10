from rest_framework import serializers
from courses.models.enrollment import Enrollment
from courses.serializers.courses import CoursesModelSerializer
from points.models.points import Points

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

class CompleteCourseSerializer(serializers.Serializer):

    enrollment_id =serializers.IntegerField(required=True)

    def validate(self, attrs):
        enrollment = Enrollment.objects.get(id=attrs["enrollment_id"])
        if enrollment.status == "P":
            points = Points.objects.get(user=enrollment.user)
            points.points += 10
            points.save()
            enrollment.status = "C"
            enrollment.save()
        return attrs