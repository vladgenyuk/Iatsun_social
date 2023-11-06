from django.contrib import admin
from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at', 'updated_at', 'image', 'publisher_id')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    fields = ('id', 'title', 'content', 'published_at', 'updated_at', 'image', 'publisher_id')


admin.site.register(Publication, PublicationAdmin)
