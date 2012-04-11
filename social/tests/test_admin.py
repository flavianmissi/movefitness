from django.contrib import admin
from django.test import TestCase

from social.admin import SocialAdmin
from social.models import Social


class SocialAdminTestCase(TestCase):

    def test_should_register_Social_model(self):
        self.assertIn(Social, admin.site._registry)

    def test_should_register_Social_model_with_SocialAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Social], SocialAdmin)
