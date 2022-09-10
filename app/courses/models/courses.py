from django.db import models


class Courses(models.Model):

    name = models.CharField(
        verbose_name="name",
        max_length=250
    )

    instructor = models.ForeignKey(
        verbose_name="User",
        to="users.User",
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        verbose_name="description",
        max_length=1000
    )

    datetime = models.DateTimeField(
        verbose_name="datetime",
        auto_now_add=False,
    )

    location = models.CharField(
        verbose_name="loactions",
        max_length=250
    )

    school = models.ForeignKey(
        verbose_name="School",
        on_delete=models.CASCADE,
        to="users.Schools",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.name