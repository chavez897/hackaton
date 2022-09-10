from django.db import models


class Points(models.Model):

    user = models.ForeignKey(
        verbose_name="User",
        to="users.User",
        on_delete=models.CASCADE,
    )

    start = models.DateTimeField(
        verbose_name="datetime",
        auto_now_add=True,
    )

    points = models.IntegerField(
        verbose_name="points",
        default=0
    )



    class Meta:
        verbose_name = "point"
        verbose_name_plural = "points"

    def __str__(self):
        return "{} - {}".format(self.user, self.points)