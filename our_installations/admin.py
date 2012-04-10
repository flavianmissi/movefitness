from django.contrib import admin

from our_installations.models import OurInstallations


class OurInstallationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(OurInstallations, OurInstallationsAdmin)
