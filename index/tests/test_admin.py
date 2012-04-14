from django.test import TestCase
from django.contrib import admin

from index.models import Image
from index.admin import ImageAdmin


class ImageAdminTestCase(TestCase):

    def test_should_register_Image_model(self):
        self.assertIn(Image, admin.site._registry)

    def test_should_register_Image_model_with_OurInstallationAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Image], ImageAdmin)
