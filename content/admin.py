from django.contrib import admin

from content.models import Content


class ContentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Content, ContentAdmin)
