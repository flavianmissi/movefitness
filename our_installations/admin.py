from django.contrib import admin

from our_installations.models import OurInstallation


class OurInstallationAdmin(admin.ModelAdmin):
    pass


admin.site.register(OurInstallation, OurInstallationAdmin)
