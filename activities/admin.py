from django.contrib import admin

from activities.models import Activity


class ActivityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Activity, ActivityAdmin)
