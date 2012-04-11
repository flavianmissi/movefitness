from django.test import TestCase
from django.contrib import admin

from contact.models import Contact
from contact.admin import ContactAdmin


class ContactAdminTestCase(TestCase):

    def test_should_register_Contact_model(self):
        self.assertIn(Contact, admin.site._registry)

    def test_should_register_Contact_model_with_OurInstallationAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Contact], ContactAdmin)

