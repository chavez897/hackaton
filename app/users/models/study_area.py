from django.db import models


class StudyArea(models.Model):

    name = models.CharField(
        verbose_name="Study Area",
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
        verbose_name = "study area"
        verbose_name_plural = "study areas"

    def __str__(self):
        """Return role."""
        return self.name