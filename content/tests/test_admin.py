from django.test import TestCase
from django.contrib import admin

from content.models import Content
from content.admin import ContentAdmin


class ContentAdminTestCase(TestCase):

    def test_should_register_Content_model(self):
        self.assertIn(Content, admin.site._registry)

    def test_should_register_Content_model_with_OurInstallationAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Content], ContentAdmin)
