from django.contrib import admin

from points.models.points import Points

@admin.register(Points)
class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "points")
    list_display_links = ("id", "user")
