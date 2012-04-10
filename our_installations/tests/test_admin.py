from django.test import TestCase
from django.contrib import admin

from our_installations.models import OurInstallations
from our_installations.admin import OurInstallationsAdmin


class OurInstallationsAdminTestCase(TestCase):

    def test_should_register_OurInstallations_model(self):
        self.assertIn(OurInstallations, admin.site._registry)

    def test_should_register_OurInstallations_model_with_OurInstallationsAdmin_class(self):
        self.assertIsInstance(admin.site._registry[OurInstallations], OurInstallationsAdmin)
