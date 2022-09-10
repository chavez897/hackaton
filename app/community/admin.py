from django.contrib import admin

from community.models.community import Community
from community.models.posts import Posts

@admin.register(Community)
class CommunityModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

@admin.register(Posts)
class PostsModelAdmin(admin.ModelAdmin):
    list_display = ("id", "community", "post")
    list_display_links = ("id", )

