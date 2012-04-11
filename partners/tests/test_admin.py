from django.test import TestCase
from django.contrib import admin

from partners.models import Partner
from partners.admin import PartnerAdmin


class PartnerAdminTestCase(TestCase):

    def test_should_register_Partner_model(self):
        self.assertIn(Partner, admin.site._registry)

    def test_should_register_Partner_model_with_PartnerAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Partner], PartnerAdmin)
