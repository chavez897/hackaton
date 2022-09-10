from django.contrib import admin

from courses.models.courses import Courses
from courses.models.enrollment import Enrollment

@admin.register(Courses)
class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("id", "name")


@admin.register(Enrollment)
class EnrollmentModelAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "user")
    list_display_links = ("id", )

