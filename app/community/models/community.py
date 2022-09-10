from django.db import models


class Community(models.Model):

    picture = models.ImageField(  # noqa DJ01
        verbose_name="Avatar",
        upload_to="community/picture/%Y/%m/%d/",
        max_length=1000,
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name="name",
        max_length=250
    )

    def __str__(self):
        return "{}".format(self.name)
