from django.contrib import admin

from social.models import Social


class SocialAdmin(admin.ModelAdmin):
    pass


admin.site.register(Social, SocialAdmin)
