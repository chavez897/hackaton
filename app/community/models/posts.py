from django.db import models


class Posts(models.Model):

    community = models.ForeignKey(
        verbose_name="Community",
        on_delete=models.CASCADE,
        to="community.Community",
        blank=True,
        null=True,
    )

    post = models.TextField(
        verbose_name="post",
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{}".format(self.post)
