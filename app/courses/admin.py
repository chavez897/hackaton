from django.contrib import admin

from courses.models.courses import Courses


@admin.register(Courses)
class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("id", "name")

