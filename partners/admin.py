from django.contrib import admin

from partners.models import Partner


class PartnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Partner, PartnerAdmin)
