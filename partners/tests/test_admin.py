from django.contrib import admin
from django.test import TestCase

from partners.admin import PartnerAdmin
from partners.models import Partner


class PartnerAdminTestCase(TestCase):

    def test_should_register_Partner_model(self):
        self.assertIn(Partner, admin.site._registry)

    def test_should_register_Partner_model_with_PartnerAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Partner], PartnerAdmin)
