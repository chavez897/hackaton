from django.db import models

class DeliveryMode(models.TextChoices):
    ONLINE = "O", "Online"
    PERSON = "P", "Person"


class Courses(models.Model):

    picture = models.ImageField(  # noqa DJ01
        verbose_name="Avatar",
        upload_to="courses/picture/%Y/%m/%d/",
        max_length=1000,
        blank=True,
        null=True,
    )
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

    delivery_mode = models.CharField(
        verbose_name="Delivery Mode",
        max_length=10,
        choices=DeliveryMode.choices,
        default=DeliveryMode.PERSON,
    )



    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.name