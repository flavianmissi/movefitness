from django.contrib import admin

from our_installations.models import OurInstallations


class OurInstallationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(OurInstallations, OurInstallationsAdmin)
