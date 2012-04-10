from django.test import TestCase
from django.contrib import admin

from our_installations.models import OurInstallation
from our_installations.admin import OurInstallationAdmin


class OurInstallationAdminTestCase(TestCase):

    def test_should_register_OurInstallation_model(self):
        self.assertIn(OurInstallation, admin.site._registry)

    def test_should_register_OurInstallation_model_with_OurInstallationAdmin_class(self):
        self.assertIsInstance(admin.site._registry[OurInstallation], OurInstallationAdmin)
