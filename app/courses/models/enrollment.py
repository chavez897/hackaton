from django.db import models

class CourseStatus(models.TextChoices):
    PROGRESS = "P", "Progress"
    COMPLETE = "C", "Complete"


class Enrollment(models.Model):

    user = models.ForeignKey(
        verbose_name="User",
        to="users.User",
        on_delete=models.CASCADE,
    )

    start = models.DateTimeField(
        verbose_name="datetime",
        auto_now_add=True,
    )

    course = models.ForeignKey(
        verbose_name="Course",
        to="courses.Courses",
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        verbose_name="Status",
        max_length=10,
        choices=CourseStatus.choices,
        default=CourseStatus.PROGRESS
    )



    class Meta:
        verbose_name = "enrollment"
        verbose_name_plural = "enrollments"

    def __str__(self):
        return "{} - {}".format(self.course, self.user)